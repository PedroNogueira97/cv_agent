from datetime import timedelta

from fastapi import APIRouter, HTTPException, status, Request
from api.database import register_user_db, get_user_db, verify_password
from api.schemas import UserRegister, UserLogin, Token
from api.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserRegister, request: Request):
    # Rate limit registration? (optional, could use @limiter.limit("5/minute"))
    if register_user_db(user.username, str(user.email), user.password):
        return {"message": "Usuário registrado com sucesso"}
    raise HTTPException(status_code=400, detail="Usuário já existe")

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = get_user_db(user.username)
    if not db_user or not verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
