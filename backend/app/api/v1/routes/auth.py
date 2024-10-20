from app.models.user import User
from app.schemas.auth import OTPVerificationRequest
from app.services.user_service import verify_otp
from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from app.services.user_service import create_access_token, get_user_by_mobile, generate_otp, create_user
from app.core.config import settings

router = APIRouter()

@router.post("/user/validateOtp")
async def validate_otp(verification_data: OTPVerificationRequest):
    user = get_user_by_mobile(verification_data.mobile)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    if not verify_otp(user.mobile, verification_data.otp):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OTP",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.mobile}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/user/login")
async def login_request(user: User):
    existing_user = get_user_by_mobile(user.mobile)
    if not existing_user:
        # Create a new user if one doesn't exist
        new_user = create_user(user)
        if not new_user:
            raise HTTPException(status_code=400, detail="Failed to create user")
        existing_user = new_user

    otp = generate_otp()
    # Store the OTP securely (e.g., in a temporary storage with expiration)
    # In a real-world scenario, you'd send this OTP to the user's mobile number
    # For this example, we'll just return it (don't do this in production!)
    return {"otp": otp}
