from .security import password_verification, to_hash, generate_auth_token, extract_auth_token
from exam.utils import getargs
from typing import Union, Iterable, Callable, Dict
from exam.security import extract_auth_token
from functools import wraps
from flask import abort


GOD_SCOPES = frozenset(['god', ])


def secured(scopes: Union[str, Iterable[str]] = (), allow_from_headers=True,
            include_god=True, else_answer=401,
            verify: Callable[[str], Dict] = extract_auth_token
            ):
    """
    Security checker decorator

    Usage:
    @route('/some/route')
    @secured(scopes='admin moderator')
    def some_route():
        ...

    or:
    @route('/some/route')
    @secured(scopes=['admin', 'moderator'], else_answer=403)
    def some_route():
        ...

    Original token and token data available inside decorated func
    by its _token and _token_data attributes if needed

    Note: scopes parameter can be iterable or string. String are splitted
    Note: 'god' scope appended to given ones by default

    :param scopes:                  allowed scopes as iterable or string
    :param allow_from_headers:      allow token lookup in request.headers
    :param include_god:             include or not GOD_SCOPES. Default is True
    :param else_answer:             passed to flask's abort func (http code or response obj)
    :param expect_base64:           expect token encoded in base64 or not, default True
    :param verify:                  a verification func. Must return payload if verified
    :return:                        throws 401 or wrapped func's results
    """

    if isinstance(scopes, str):
        scopes = scopes.split()
    if include_god:
        _scopes = set(scopes).union(GOD_SCOPES)

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

            tscopes = set(token_data.get('scopes', ()))
            if not _scopes.intersection(tscopes):
                return abort(else_answer)

            wrapper._token = token
            wrapper._token_data = token_data

            return f(*args, **kwargs)
        return wrapper
    return wrapper_of_wrapper