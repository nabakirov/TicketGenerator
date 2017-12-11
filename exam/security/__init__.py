from .security import password_verification, to_hash, generate_auth_token, extract_auth_token
from exam.utils import getargs
from typing import Callable, Dict
from exam.security import extract_auth_token
from functools import wraps
from flask import abort


def secured(allow_from_headers=True, else_answer=401,
            verify: Callable[[str], Dict] = extract_auth_token
            ):

    def wrapper_of_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            from flask import request

            t, jwt = getargs(request, 'token', 'jwt')
            token = t or jwt

            if not token and allow_from_headers:
                token = request.headers.get('Authorization', '')
                if token.startswith('Bearer '):
                    token = token[7:]

            if not token:
                return abort(else_answer)

            token_data = verify(token)
            if not token_data:
                return abort(else_answer)

            wrapper._token = token
            wrapper._token_data = token_data

            return f(*args, **kwargs)
        return wrapper
    return wrapper_of_wrapper
