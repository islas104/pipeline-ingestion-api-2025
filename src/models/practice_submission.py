from sqlalchemy import Column, Integer, String, Date, Float, Boolean, Text
from src.database import Base

class PracticeSubmission(Base):
    __tablename__ = "practice_submissions"

    id = Column(Integer, primary_key=True, index=True)

    # Core identifying fields
    farmer_unique_code = Column(Text, nullable=True)
    display_field_id = Column(Text, nullable=True)
    growing_year = Column(Integer, nullable=True)
    planting_date = Column(Date, nullable=True)
    enrollment_date = Column(Date, nullable=True)

    # Cotton harvest
    production_volume = Column(Integer, nullable=True)
    residue_harvested = Column(Text, nullable=True)
    residue_burned = Column(Text, nullable=True)
    residue_shredded = Column(Text, nullable=True)
    residue_shredded_fuel = Column(Text, nullable=True)
    other_residue_shredded_fuel = Column(Text, nullable=True)
    residue_shredded_usage = Column(Float, nullable=True)

    # Land preparation
    number_of_events = Column(Float, nullable=True)
    type_of_event = Column(Text, nullable=True)
    date_land = Column(Date, nullable=True)
    power_by_land = Column(Text, nullable=True)
    other_power_by = Column(Text, nullable=True)
    fuel_usage_litres = Column(Float, nullable=True)
    hours_of_animal_tillage = Column(Float, nullable=True)
    animal_ploughing = Column(Boolean, nullable=True)

    # Irrigation
    number_of_irrigation_events = Column(Integer, nullable=True)
    irrigation_method = Column(Text, nullable=True)
    other_irrigation_method = Column(Text, nullable=True)
    electricity_bill = Column(Text, nullable=True)

    # Fertilisers (minimal subset)
    number_of_fertiliser_events = Column(Integer, nullable=True)
    fertiliser_category_type = Column(Text, nullable=True)
    other_product_type = Column(Text, nullable=True)
    brand_name_fertilisers = Column(Text, nullable=True)
    quantity_fertilisers = Column(Float, nullable=True)

    # Chemistry
    number_of_applications = Column(Integer, nullable=True)
    chemical_category_chemistry = Column(Text, nullable=True)
    product_name_chemistry_other = Column(Text, nullable=True)
    quantity_chemistry = Column(Float, nullable=True)

    # Landscape
    land_converted_20_years = Column(Text, nullable=True)
    other_land_converted = Column(Text, nullable=True)
    out_surface_activities = Column(Text, nullable=True)
    other_surface_activities = Column(Text, nullable=True)
