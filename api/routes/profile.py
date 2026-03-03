from fastapi import APIRouter, Depends
from api.database import save_user_profile_db, load_user_profile_db
from api.schemas import UserProfile
from api.auth import get_current_user

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/")
def get_profile(current_user: str = Depends(get_current_user)):
    profile = load_user_profile_db(current_user)
    return profile

@router.post("/")
def save_profile(profile: UserProfile, current_user: str = Depends(get_current_user)):
    save_user_profile_db(current_user, profile.model_dump())
    return {"message": "Perfil atualizado"}
