import jwt
import datetime
from django.conf import settings


def create_token(payload, timeout):
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    salt = settings.SECRET_KEY
    token = jwt.encode(payload=payload, key=salt, algorithm="HS256")
    return token
