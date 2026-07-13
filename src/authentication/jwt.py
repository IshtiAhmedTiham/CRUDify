from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "hello ji, i am ishti ahmed"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def encode_token(data : dict):
    to_encode = data.copy()

    EXPIRE_TIME = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : EXPIRE_TIME})

    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="src/authentication/auth.py")

def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None
