from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Lab 12 Full Stack GenAI"
)

app.include_router(router)