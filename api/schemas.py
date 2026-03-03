from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel) :
    username: str
    password: str

class UserProfile(BaseModel):
    nome: str = ""
    email: str = ""
    telefone: str = ""
    linkedin: str = ""
    github: str = ""
    formacao: str = ""
    stack: str = ""
    projetos: str = ""
    experiencia: str = ""
    idiomas: str = ""
    cursos: str = ""

class ChatRequest(BaseModel):
    prompt: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str

class Token(BaseModel):
    access_token: str
    token_type: str
