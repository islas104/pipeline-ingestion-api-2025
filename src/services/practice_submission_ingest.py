import pandas as pd
from sqlalchemy.orm import Session
from src.models.practice_submission import PracticeSubmission
from datetime import datetime

def safe_date(val):
    if pd.isna(val) or val == "":
        return None
    try:
        return pd.to_datetime(val).date()
    except Exception:
        return None

def safe_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

def ingest_practice_submissions(csv_path: str, db: Session) -> int:
    df = pd.read_csv(csv_path)

    inserted = 0

    for _, row in df.iterrows():
        submission = PracticeSubmission(
            farmer_unique_code=row.get("farmer_unique_code"),
            display_field_id=row.get("display_field_id"),
            growing_year=safe_int(row.get("growing_year")),
            planting_date=safe_date(row.get("planting_date")),
            enrollment_date=safe_date(row.get("enrollment_date")),
            production_volume=safe_int(row.get("production_volume")),
            residue_harvested=row.get("residue_harvested"),
            residue_burned=row.get("residue_burned"),
            residue_shredded=row.get("residue_shredded"),
            residue_shredded_fuel=row.get("residue_shredded_fuel"),
            other_residue_shredded_fuel=row.get("other_residue_shredded_fuel"),
            residue_shredded_usage=safe_float(row.get("residue_shredded_usage")),
            number_of_events=safe_float(row.get("number_of_events")),
            type_of_event=row.get("type_of_event"),
            date_land=safe_date(row.get("date_land")),
            power_by_land=row.get("power_by_land"),
            other_power_by=row.get("other_power_by"),
            fuel_usage_litres=safe_float(row.get("fuel_usage_litres")),
            hours_of_animal_tillage=safe_float(row.get("hours_of_animal_tillage")),
            animal_ploughing=row.get("animal_ploughing") in ["True", "true", True],
            number_of_irrigation_events=safe_int(row.get("number_of_irrigation_events")),
            irrigation_method=row.get("irrigation_method"),
            other_irrigation_method=row.get("other_irrigation_method"),
            electricity_bill=row.get("electricity_bill"),
            number_of_fertiliser_events=safe_int(row.get("number_of_fertiliser_events")),
            fertiliser_category_type=row.get("fertiliser_category_type"),
            other_product_type=row.get("other_product_type"),
            brand_name_fertilisers=row.get("brand_name_fertilisers"),
            quantity_fertilisers=safe_float(row.get("quantity_fertilisers")),
            number_of_applications=safe_int(row.get("number_of_applications")),
            chemical_category_chemistry=row.get("chemical_category_chemistry"),
            product_name_chemistry_other=row.get("product_name_chemistry_other"),
            quantity_chemistry=safe_float(row.get("quantity_chemistry")),
            land_converted_20_years=row.get("land_converted_20_years"),
            other_land_converted=row.get("other_land_converted"),
            out_surface_activities=row.get("out_surface_activities"),
            other_surface_activities=row.get("other_surface_activities"),
        )

        db.add(submission)
        inserted += 1

    db.commit()
    return inserted
