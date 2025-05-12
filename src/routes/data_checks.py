from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.data_checks import run_data_checks
from src.services.other_responses_report import get_other_responses_report
from src.services.field_summary_report import get_field_summary_report

router = APIRouter()

@router.post("/run-checks")
def run_checks_endpoint(db: Session = Depends(get_db)):
    results = run_data_checks(db)
    return {"checks": results}

@router.get("/report/other-responses")
def report_other_responses(db: Session = Depends(get_db)):
    return get_other_responses_report(db)

@router.get("/report/field-summary")
def report_field_summary(db: Session = Depends(get_db)):
    return get_field_summary_report(db)