from fastapi import APIRouter
from app.database import goals_collection
from app.schemas import GoalCreate


router = APIRouter()

@router.post("/goals")
async def create_goal(goal : GoalCreate):
    await goals_collection.insert_one(goal.dict())
    return {"message": "Goal created successfully"}


@router.get("/goals")
async def get_goals():
    goals = []
    async for goal in goals_collection.find():
        goal["_id"] = str(goal["_id"])
        goals.append(goal)
        return goals
    
    