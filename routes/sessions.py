from fastapi import APIRouter
from app.database import sessions_collection
from app.schemas import SessionCreate

router = APIRouter()

@router.post("/sessions")
async def log_session(session: SessionCreate):
    await sessions_collection.insert_one(session.dict())
    return {"message": "Session logged"}

@router.get("/sessions")
async def get_sessions():
    sessions = []
    async for session in sessions_collection.find():
        session["_id"] = str(session["_id"])
        sessions.append(session)
    return sessions