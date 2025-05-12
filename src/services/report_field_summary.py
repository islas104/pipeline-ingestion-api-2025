import pandas as pd
import os
from sqlalchemy.orm import Session
from src.models.field_submission import FieldSubmission

def generate_field_summary_report(db: Session) -> str:
    records = db.query(FieldSubmission).all()

    rows = []
    for r in records:
        rows.append({
            "Farmer_unique_code": r.Farmer_unique_code,
            "display_field_id": r.display_field_id,
            "shape_area_note": r.shape_area_note,
            "irrigation_type": "Irrigated" if r.Number_of_irrigation_events and r.Number_of_irrigation_events > 0 else "Rainfed",
            "animal_ploughing": "Yes" if r.hours_of_animal_tillage and r.hours_of_animal_tillage > 0 else "No"
        })

    df = pd.DataFrame(rows)
    output_path = os.path.join("src", "reports", "field_summary.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

