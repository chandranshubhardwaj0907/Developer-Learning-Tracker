from fastapi import FastAPI
from routes import goals, sessions, reports

app = FastAPI(title="Developer Learning Tracker API")

app.include_router(goals.router)
app.include_router(sessions.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {"status": "Learning Tracker API running"}
