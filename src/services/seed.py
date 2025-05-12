from src.models.field_submission import FieldSubmission
from src.database import SessionLocal
from datetime import datetime

def seed_field_submissions():
    db = SessionLocal()

    # Sample farmer and field IDs matching your CSV
    sample_data = [
        {"Farmer_unique_code": f"FARMER00{i}", "display_field_id": f"FIELD00{i}"} for i in range(1, 11)
    ]

    for entry in sample_data:
        existing = db.query(FieldSubmission).filter_by(
            Farmer_unique_code=entry["Farmer_unique_code"],
            display_field_id=entry["display_field_id"]
        ).first()

        if not existing:
            submission = FieldSubmission(
                Farmer_unique_code=entry["Farmer_unique_code"],
                display_field_id=entry["display_field_id"],
                Enrollment_date=None,  # will be updated by ingest
                shape_area_note=None,
                Number_of_irrigation_events=None,
                hours_of_animal_tillage=None,
                state_IPs=None,
                Implementing_partner_s=None,
            )
            db.add(submission)

    db.commit()
    db.close()
    print("✅ Seed data inserted.")

# Run this manually from Python shell if needed:
# >>> from src.services.seed import seed_field_submissions
# >>> seed_field_submissions()
