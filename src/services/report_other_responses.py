from sqlalchemy.orm import Session
import pandas as pd
import os
from src.models.field_submission import FieldSubmission
from deep_translator import GoogleTranslator

def generate_other_responses_report(db: Session) -> str:
    other_columns = [
        "other_power_by", "other_water_source", "other_irrigation_method",
        "other_irrigation_power", "other_product_type", "other_residue_shredded_fuel",
        "product_name_chemistry_other", "other_land_converted", "other_surface_activities"
    ]

    query = db.query(FieldSubmission)
    rows = []

    for record in query:
        for column in other_columns:
            value = getattr(record, column, None)
            if value and value.strip():
                translated = GoogleTranslator(source='auto', target='en').translate(text=value)
                rows.append({
                    "Farmer_unique_code": record.Farmer_unique_code,
                    "display_field_id": record.display_field_id,
                    "field_name": column,
                    "original_value": value,
                    "translated_value": translated
                })

    if not rows:
        return "No 'other_' responses found."

    df = pd.DataFrame(rows)
    output_path = os.path.join("src", "reports", "other_responses.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
