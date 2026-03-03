from fastapi import APIRouter, Depends, HTTPException
from api.database import load_user_profile_db
from api.schemas import ChatRequest, ChatResponse
from api.auth import get_current_user
from agent import get_agent

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, current_user: str = Depends(get_current_user)):
    user_data = load_user_profile_db(current_user)
    if not user_data.get("nome"):
        raise HTTPException(status_code=400, detail="Perfil não preenchido")
    
    try:
        agent = get_agent(user_data, user_id=current_user, session_id=request.session_id)
        response = agent.run(request.prompt)
        return ChatResponse(response=response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
