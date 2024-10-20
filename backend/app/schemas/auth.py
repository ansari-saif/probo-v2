from pydantic import BaseModel

class LoginRequest(BaseModel):
    mobile: str

class OTPVerificationRequest(BaseModel):
    mobile: str
    otp: str
