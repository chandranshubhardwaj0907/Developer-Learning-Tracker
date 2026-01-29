from fastapi import APIRouter
from app.database import sessions_collection

router = APIRouter()


@router.get("/weekly-summary")
async def weekly_summary():
    pipeline = [{"$group": {"_id": "$goal_title", "total_hours": {"$sum": "$hours"}}}]

    result = []
    async for doc in sessions_collection.aggregate(pipeline):
        result.append(doc)

    return result
