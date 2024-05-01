from fastapi import APIRouter

router = APIRouter()

@router.post("/process-audio")
def process_audio():
    return {"message": "Audio processed"}
