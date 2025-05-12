from sqlalchemy.orm import Session
from src.models.practice_submission import PracticeSubmission
from typing import List, Dict

def get_other_responses_report(db: Session) -> List[Dict]:
    fields_to_check = [
        ("other_residue_shredded_fuel", "Residue Shredded Fuel (Other)"),
        ("other_power_by", "Power Source (Other)"),
        ("other_product_type", "Fertiliser Product Type (Other)"),
        ("product_name_chemistry_other", "Chemical Product Name (Other)"),
        ("other_water_source", "Water Source (Other)"),
        ("other_irrigation_method", "Irrigation Method (Other)"),
        ("other_irrigation_power", "Irrigation Power (Other)"),
        ("other_land_converted", "Land Converted Description (Other)"),
        ("other_surface_activities", "Runoff Management Description (Other)")
    ]

    results = []

    for field_name, label in fields_to_check:
        records = db.query(PracticeSubmission).filter(getattr(PracticeSubmission, field_name).isnot(None)).all()
        for r in records:
            results.append({
                "field": field_name,
                "label": label,
                "value": getattr(r, field_name),
                "farmer": r.farmer_unique_code,
                "field_id": r.display_field_id
            })

    return results
