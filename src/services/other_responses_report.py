from sqlalchemy.orm import Session
from src.models.practice_submission import PracticeSubmission
from typing import List, Dict
from collections import defaultdict

TRANSLATION_MAP = {
    "યુરિયા": "Urea",
    "યુરિયા અને પોટાશ": "Urea and Potash",
    "यूरिया": "Urea",
    
}

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

    grouped = defaultdict(lambda: {
        "count": 0,
        "farmers": set(),
        "fields": set()
    })

    for field_name, label in fields_to_check:
        records = db.query(PracticeSubmission).filter(getattr(PracticeSubmission, field_name).isnot(None)).all()
        for r in records:
            raw_value = getattr(r, field_name).strip()
            translated = TRANSLATION_MAP.get(raw_value, raw_value)
            key = (label, translated)

            grouped[key]["count"] += 1
            grouped[key]["farmers"].add(r.farmer_unique_code)
            grouped[key]["fields"].add(r.display_field_id)

    results = []
    for (label, translated_value), data in grouped.items():
        results.append({
            "question": label,
            "translated_response": translated_value,
            "count": data["count"],
            "example_farmer": next(iter(data["farmers"])),
            "example_field_id": next(iter(data["fields"]))
        })

    return results
