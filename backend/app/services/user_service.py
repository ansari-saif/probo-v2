from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings
from app.models.user import User, UserCreate
from sqlmodel import Session, select
from app.core.database import engine
import pyotp

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_otp():
    return "123456"
    totp = pyotp.TOTP(settings.OTP_SECRET_KEY, interval=300)  # 5-minute OTP
    return totp.now()

def verify_otp(mobile: str, otp: str):
    # In a real-world scenario, you should retrieve the OTP from a secure temporary storage
    # and verify it against the provided OTP
    # For this example, we'll use a fixed secret key (don't do this in production!)

    return otp == "123456"
    totp = pyotp.TOTP(settings.OTP_SECRET_KEY, interval=300)
    return totp.verify(otp)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        mobile: str = payload.get("sub")
        if mobile is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_mobile(mobile)
    if user is None:
        raise credentials_exception
    return user

def get_user_by_mobile(mobile: str):
    with Session(engine) as session:
        statement = select(User).where(User.mobile == mobile)
        user = session.exec(statement).first()
    return user

def create_user(user: UserCreate):
    with Session(engine) as session:
        user.balance = 15
        db_user = User.from_orm(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user

def authenticate_user(mobile: str, otp: str):
    user = get_user_by_mobile(mobile)
    if not user:
        return False
    if not verify_otp(otp, mobile):
        return False
    return user
