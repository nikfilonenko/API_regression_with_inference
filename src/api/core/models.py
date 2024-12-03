from pydantic import BaseModel
from typing import List, Optional

class Car(BaseModel):
    name: str
    year: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: float
    engine: int
    max_power: float
    torque: float
    seats: int
    max_torque_rpm: float

class Cars(BaseModel):
    objects: List[Car]