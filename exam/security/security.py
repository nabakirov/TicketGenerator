from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from exam.configs import SECRET_KEY


def password_verification(password, hash_password):
    return pwd_context.verify(password, hash_password)


def to_hash(password):
    return pwd_context.encrypt(password)


def generate_auth_token(data, secret_key=SECRET_KEY, expiration=60 * 60):
    s = Serializer(secret_key, expires_in=expiration)
    return s.dumps(data)


def extract_auth_token(token, secret_key=SECRET_KEY):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    if 'data' in data:
        return data['data']
    return data
