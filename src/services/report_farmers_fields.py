import pandas as pd
import os
from sqlalchemy.orm import Session
from src.models.field_submission import FieldSubmission
from sqlalchemy import func

def generate_farmer_field_report(db: Session) -> str:
    rows = []

    records = db.query(FieldSubmission).all()
    for r in records:
        rows.append({
            "Farmer_unique_code": r.Farmer_unique_code,
            "display_field_id": r.display_field_id,
            "shape_area_note": r.shape_area_note,
        })

    df = pd.DataFrame(rows)
    df["shape_area_note"] = df["shape_area_note"].fillna(0)

    # Group by farmer
    summary = (
        df.groupby("Farmer_unique_code")
        .agg({
            "display_field_id": "count",
            "shape_area_note": "sum"
        })
        .rename(columns={"display_field_id": "field_count", "shape_area_note": "total_hectares"})
        .reset_index()
    )

    output_path = os.path.join("src", "reports", "farmer_field_mapping.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    summary.to_csv(output_path, index=False)
    return output_path
