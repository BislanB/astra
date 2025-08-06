from fastapi import FastAPI, Depends, HTTPException
from core.db import get_db

app = FastAPI()

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}

@app.get("/admin/export")
async def export_reports(
    db: Session = Depends(get_db),
    auth: str = Header(None)
):
    if auth != config.ADMIN_SECRET:
        raise HTTPException(403)
    
    return FileResponse("reports.csv")