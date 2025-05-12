from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.practice_submission import PracticeSubmissionCreate, PracticeSubmissionRead
from src.models.practice_submission import PracticeSubmission

router = APIRouter(
    prefix="/practice-submissions",
    tags=["Practice Submissions"]
)

@router.post("/", response_model=PracticeSubmissionRead)
def create_submission(submission: PracticeSubmissionCreate, db: Session = Depends(get_db)):
    try:
        db_submission = PracticeSubmission(**submission.dict())
        db.add(db_submission)
        db.commit()
        db.refresh(db_submission)
        return db_submission
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create submission: {str(e)}")
