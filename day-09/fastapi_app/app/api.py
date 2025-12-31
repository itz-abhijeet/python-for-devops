from fastapi import FastAPI
from routers import metrics, log, aws

app = FastAPI(
    title = "DevOps Utils",
    description = "This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version = "1.0.0",
    doc_url = "/docs",
    redoc = "/redoc"
)

@app.get("/")
def welcome():
    """
    This is an Welcome API 
    """
    return {"message":"Welcome"}

app.include_router(metrics.router)
app.include_router(log.router)
app.include_router(aws.router, prefix="/aws")