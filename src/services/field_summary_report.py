from sqlalchemy.orm import Session
from src.models.practice_submission import PracticeSubmission
from typing import List, Dict

def get_field_summary_report(db: Session) -> List[Dict]:
    fields = db.query(PracticeSubmission).all()
    summary = []

    for field in fields:
        summary.append({
            "display_field_id": field.display_field_id,
            "state": field.state_IPs,
            "hectares": field.shape_area_note,
            "irrigation_status": "Irrigated" if (field.number_of_irrigation_events or 0) > 0 else "Rainfed",
            "animal_ploughing": "Yes" if (field.hours_of_animal_tillage or 0) > 0 else "No"
        })

    return summary
