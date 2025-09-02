from fastapi import HTTPException

def validate_email(email: str):
    if "@" not in email or "." not in email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    return email

def validate_password(password: str):
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password too short")
    return password
