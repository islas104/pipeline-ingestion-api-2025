def update_field_area_from_csv(file_path: str, db: Session):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stmt = (
                update(FieldSubmission)
                .where(FieldSubmission.display_field_id == row["display_field_id"])
                .values(shape_area_note=row["shape_area_note"])
            )
            db.execute(stmt)
    db.commit()