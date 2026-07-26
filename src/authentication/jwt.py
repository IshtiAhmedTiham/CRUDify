from jose import jwt
from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "hello-ji-i-am-ishti-ahmed-tiham"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_schema = OAuth2PasswordBearer(tokenUrl="src/authentication/auth")


def encode_jwt(data : dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm = ALGORITHM
    )

    return token


def decode_jwt(token : str):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms = [ALGORITHM]
    )

    return payload