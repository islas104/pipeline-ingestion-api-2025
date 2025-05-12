from sqlalchemy.orm import Session
from typing import List, Dict
from sqlalchemy import func

from src.models.practice_submission import PracticeSubmission
from src.models.field_submission import FieldSubmission


def run_data_checks(db: Session) -> List[Dict]:
    checks_summary = []

    # Check 1: Missing planting date
    missing_planting = db.query(PracticeSubmission).filter(
        PracticeSubmission.planting_date.is_(None)
    ).all()
    if missing_planting:
        checks_summary.append({
            "check": "Missing Planting Date",
            "issues_found": len(missing_planting),
            "affected_farmers": [r.farmer_unique_code for r in missing_planting]
        })

    # Check 2: Irrigation method present but 0 irrigation events
    irrigation_mismatch = db.query(PracticeSubmission).filter(
        PracticeSubmission.number_of_irrigation_events == 0,
        PracticeSubmission.irrigation_method.isnot(None)
    ).all()
    if irrigation_mismatch:
        checks_summary.append({
            "check": "Irrigation Method Specified but Events = 0",
            "issues_found": len(irrigation_mismatch),
            "affected_fields": [r.display_field_id for r in irrigation_mismatch]
        })

    # Check 3: Animal tillage hours > 0 but marked as no animal ploughing
    animal_mismatch = db.query(PracticeSubmission).filter(
        PracticeSubmission.animal_ploughing == False,
        PracticeSubmission.hours_of_animal_tillage > 0
    ).all()
    if animal_mismatch:
        checks_summary.append({
            "check": "Animal Tillage Hours > 0 but animal_ploughing is False",
            "issues_found": len(animal_mismatch),
            "affected_fields": [r.display_field_id for r in animal_mismatch]
        })

    # Check 4: Missing production volume
    missing_volume = db.query(PracticeSubmission).filter(
        PracticeSubmission.production_volume.is_(None)
    ).all()
    if missing_volume:
        checks_summary.append({
            "check": "Missing Production Volume",
            "issues_found": len(missing_volume),
            "affected_farmers": [r.farmer_unique_code for r in missing_volume]
        })

    # Check 5: Fertiliser events > 0 but quantity is null
    fertiliser_mismatch = db.query(PracticeSubmission).filter(
        PracticeSubmission.number_of_fertiliser_events > 0,
        PracticeSubmission.quantity_fertilisers.is_(None)
    ).all()
    if fertiliser_mismatch:
        checks_summary.append({
            "check": "Fertiliser Events > 0 but Quantity is Null",
            "issues_found": len(fertiliser_mismatch),
            "affected_farmers": [r.farmer_unique_code for r in fertiliser_mismatch]
        })

    # Check 6: Farmers with multiple fields
    multi_fields = (
        db.query(FieldSubmission.Farmer_unique_code)
        .group_by(FieldSubmission.Farmer_unique_code)
        .having(func.count(FieldSubmission.display_field_id) > 1)
        .all()
    )
    if multi_fields:
        checks_summary.append({
            "check": "Farmers with Multiple Fields",
            "issues_found": len(multi_fields),
            "farmer_codes": [row[0] for row in multi_fields]
        })

    # Check 7: Missing growing year
    missing_growing_year = db.query(PracticeSubmission).filter(
        PracticeSubmission.growing_year.is_(None)
    ).all()
    if missing_growing_year:
        checks_summary.append({
            "check": "Missing Growing Year",
            "issues_found": len(missing_growing_year),
            "affected_farmers": [r.farmer_unique_code for r in missing_growing_year]
        })

    # Check 8: Unusually high production volume
    high_production = db.query(PracticeSubmission).filter(
        PracticeSubmission.production_volume > 5000
    ).all()
    if high_production:
        checks_summary.append({
            "check": "Production Volume > 5000kg",
            "issues_found": len(high_production),
            "affected_fields": [r.display_field_id for r in high_production]
        })

    # Check 9: Duplicate submissions for same field and year
    duplicates = (
        db.query(
            PracticeSubmission.farmer_unique_code,
            PracticeSubmission.display_field_id,
            PracticeSubmission.growing_year,
            func.count().label("count")
        )
        .group_by(
            PracticeSubmission.farmer_unique_code,
            PracticeSubmission.display_field_id,
            PracticeSubmission.growing_year
        )
        .having(func.count() > 1)
        .all()
    )
    if duplicates:
        checks_summary.append({
            "check": "Duplicate Field-Year Submissions",
            "issues_found": len(duplicates),
            "duplicates": [
                {
                    "farmer": row[0],
                    "field": row[1],
                    "year": row[2],
                    "count": row[3]
                } for row in duplicates
            ]
        })

    return checks_summary
