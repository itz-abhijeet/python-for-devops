from fastapi import APIRouter, HTTPException
from services.aws_service import show_buckets, show_instances
router = APIRouter()

@router.get("/s3", status_code=200)
def get_buckets():
    try:
        s3 = show_buckets()
        return s3
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

@router.get("/ec2", status_code=200)
def get_instances():
    try:
        ec2 = show_instances()
        return ec2
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )