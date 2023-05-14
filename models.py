from pydantic import BaseModel
from enum import Enum
class Conditon( str,Enum):
    Mint = "Mint"
    Good = "Good"
    Fair = "Fair"
    Poor = "Poor"
    Damaged = "Damaged"

class MatchBoxCar(BaseModel):
    Name: str
    Color: str
    Manufacture_Date: int
    Quality: Conditon

