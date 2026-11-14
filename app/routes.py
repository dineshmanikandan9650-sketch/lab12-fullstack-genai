from fastapi import APIRouter
from app.models import QueryRequest
from app.rag_service import generate_answer

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "running"}


@router.post("/ask")
def ask_question(request: QueryRequest):
    return generate_answer(request.question)