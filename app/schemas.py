from pydantic import BaseModel
from datetime import date


class GoalCreate(BaseModel):
    title: str
    description: str


class SessionCreate(BaseModel):
    goal_title: str
    hours: float
    session_date: date
    
    