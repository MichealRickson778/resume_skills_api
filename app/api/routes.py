from fastapi import APIRouter, UploadFile, HTTPException
from app.services.llm_service import LLMService
from app.services.pdf_service import extract_text_from_pdf
from app.services.vector_db import store_skills, retrieve_skills
from app.core.config import settings

router = APIRouter()
llm_service = LLMService(api_key=settings.LLM_API_KEY)

@router.post("/upload-resume")
async def upload_resume(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    try:
        text = extract_text_from_pdf(file)
        skills = llm_service.extract_skills(text)
        store_skills(file.filename, skills)
        return {"message": "Skills extracted", "resume_id": file.filename}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.get("/skills/{resume_id}")
async def get_skills(resume_id: str):
    try:
        skills = retrieve_skills(resume_id)
        return {"skills": skills}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/health")
async def health():
    return {"status": "healthy"}
