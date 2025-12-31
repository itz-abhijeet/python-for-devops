from fastapi import APIRouter, HTTPException
from services.log_service import summarize_logs

router = APIRouter()

@router.get("/logs",status_code=200)
def get_logs():

    try:
        logs = summarize_logs()
        return logs
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
