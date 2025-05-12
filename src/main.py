import os
import sys
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Ensure Python finds `src/` as a package
sys.path.append(os.path.abspath("src"))

from src.database import SessionLocal
from src.routes import data_checks
from src.services.enrollment_csv import ingest_enrollment_dates
from src.services.report_other_responses import generate_other_responses_report
from src.services.report_field_summary import generate_field_summary_report
from src.services.report_farmers_fields import generate_farmer_field_report

app = FastAPI(title="Unlock Practice Validation API")

# Root endpoint (optional welcome message)
@app.get("/")
def read_root():
    return {"message": "Unlock Practice Validation API is running."}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model
class UploadRequest(BaseModel):
    file_path: str

# Upload endpoint
@app.post("/upload/enrollment-date/")
def upload_enrollment_data(request: UploadRequest, db: Session = Depends(get_db)):
    filename = os.path.basename(request.file_path)
    full_path = os.path.join("src/data", filename)

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail=f"File not found: {full_path}")

    updated = ingest_enrollment_dates(full_path, db)
    return {"updated_records": updated}

# Report: "Other" responses
@app.get("/report/other-responses/")
def run_other_responses_report(db: Session = Depends(get_db)):
    report_path = generate_other_responses_report(db)
    return {"report_path": report_path}

# Report: Field summary
@app.get("/report/field-summary/")
def run_field_summary_report(db: Session = Depends(get_db)):
    report_path = generate_field_summary_report(db)
    return {"report_path": report_path}

# Report: Farmer-field mapping
@app.get("/report/farmer-field-mapping/")
def run_farmer_field_report(db: Session = Depends(get_db)):
    report_path = generate_farmer_field_report(db)
    return {"report_path": report_path}

# Stubbed data validation checks
def run_data_checks(db: Session):
    return [
        {"check": "Missing planting date", "result": "OK"},
        {"check": "Irrigation with 0 events", "result": "Issues found"},
    ]

# Run data checks
@app.get("/validation/data-checks/")
def run_all_checks(db: Session = Depends(get_db)):
    try:
        summary = run_data_checks(db)
        return {"checks_run": len(summary), "results": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# List all data checks
@app.get("/validation/checks/")
def view_all_checks():
    return {
        "checks": [
            {"name": "Missing planting date", "editable": False},
            {"name": "Irrigation with 0 events", "editable": False},
            {"name": "Animal tillage mismatch", "editable": False},
            {"name": "Missing production volume", "editable": False},
            {"name": "Fertiliser quantity missing", "editable": False},
            {"name": "Duplicate field-year submission", "editable": False},
            {"name": "Missing growing year", "editable": False},
            {"name": "High production volume", "editable": False},
            {"name": "Multiple fields per farmer", "editable": False}
        ]
    }

# Include any modular routers
app.include_router(data_checks.router)
