from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt

from app.database import SessionLocal
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(User).filter(User.username == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=401)
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

def admin_only(user=Depends(get_current_user)):
    if user.role != "ADMIN":
        raise HTTPException(status_code=403)
    return user
