from sqlalchemy import Column, String, DateTime
from src.database import Base

class FieldSubmission(Base):
    __tablename__ = "field_submissions"

    Farmer_unique_code = Column(String, primary_key=True)
    display_field_id = Column(String, primary_key=True)
    Enrollment_date = Column(DateTime, nullable=True)
