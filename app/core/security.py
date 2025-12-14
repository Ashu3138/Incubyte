import bcrypt
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "secret-key-change-later"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60

def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
