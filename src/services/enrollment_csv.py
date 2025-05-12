import pandas as pd
from datetime import datetime
from sqlalchemy.orm import Session
from src.models.field_submission import FieldSubmission


def ingest_enrollment_dates(file_path: str, db: Session) -> int:
    """
    Ingest enrollment dates from a CSV file and update corresponding records in the database.

    Args:
        file_path (str): Path to the CSV file.
        db (Session): SQLAlchemy session.

    Returns:
        int: Number of records successfully updated.
    """
    df = pd.read_csv(file_path)

    required_columns = {"Farmer_unique_code", "display_field_id", "Enrollment_date"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_columns}")

    updated_count = 0

    for _, row in df.iterrows():
        farmer_code = row.get("Farmer_unique_code")
        field_id = row.get("display_field_id")
        raw_date = row.get("Enrollment_date")

        if pd.isna(farmer_code) or pd.isna(field_id) or pd.isna(raw_date):
            continue

        try:
            parsed_date = pd.to_datetime(raw_date, errors="coerce")
            if pd.isna(parsed_date):
                continue
        except Exception:
            continue

        record = db.query(FieldSubmission).filter_by(
            Farmer_unique_code=farmer_code,
            display_field_id=field_id
        ).first()

        if record:
            record.Enrollment_date = parsed_date
            updated_count += 1

    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise RuntimeError("Failed to commit enrollment updates") from e

    return updated_count
