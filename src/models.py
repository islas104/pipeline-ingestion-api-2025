from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from src.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    odk_id = Column(String, unique=True, index=True)
    data = Column(Text, nullable=True)
    geolocation = Column(Geometry("POINT", srid=4326), nullable=True)
    farmer_photo = Column(Text, nullable=True)

    field_submissions = relationship("FieldSubmission", back_populates="submission")


class FieldSubmission(Base):
    __tablename__ = "field_submissions"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    submission = relationship("Submission", back_populates="field_submissions")

    Farmer_unique_code = Column(String, index=True)
    display_field_id = Column(String, index=True)
    Enrollment_date = Column(DateTime, nullable=True)

    shape_area_note = Column(Float, nullable=True)
    Number_of_irrigation_events = Column(Integer, nullable=True)
    hours_of_animal_tillage = Column(Float, nullable=True)
    state_IPs = Column(String, nullable=True)
    Implementing_partner_s = Column(String, nullable=True)

    # ✅ New fields
    other_irrigation_method = Column(String, nullable=True)
    other_animal_type = Column(String, nullable=True)
    other_implement_used = Column(String, nullable=True)
