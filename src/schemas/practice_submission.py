from pydantic import BaseModel
from typing import Optional
from datetime import date

class PracticeSubmissionCreate(BaseModel):
    farmer_unique_code: Optional[str]
    display_field_id: Optional[str]
    growing_year: Optional[int]
    planting_date: Optional[date]
    enrollment_date: Optional[date]
    production_volume: Optional[int]
    residue_harvested: Optional[str]
    residue_burned: Optional[str]
    residue_shredded: Optional[str]
    residue_shredded_fuel: Optional[str]
    other_residue_shredded_fuel: Optional[str]
    residue_shredded_usage: Optional[float]
    number_of_events: Optional[float]
    type_of_event: Optional[str]
    date_land: Optional[date]
    power_by_land: Optional[str]
    other_power_by: Optional[str]
    fuel_usage_litres: Optional[float]
    hours_of_animal_tillage: Optional[float]
    animal_ploughing: Optional[bool]
    number_of_irrigation_events: Optional[int]
    irrigation_method: Optional[str]
    other_irrigation_method: Optional[str]
    electricity_bill: Optional[str]
    number_of_fertiliser_events: Optional[int]
    fertiliser_category_type: Optional[str]
    other_product_type: Optional[str]
    brand_name_fertilisers: Optional[str]
    quantity_fertilisers: Optional[float]
    number_of_applications: Optional[int]
    chemical_category_chemistry: Optional[str]
    product_name_chemistry_other: Optional[str]
    quantity_chemistry: Optional[float]
    land_converted_20_years: Optional[str]
    other_land_converted: Optional[str]
    out_surface_activities: Optional[str]
    other_surface_activities: Optional[str]

class PracticeSubmissionRead(PracticeSubmissionCreate):
    id: int

    class Config:
        orm_mode = True
