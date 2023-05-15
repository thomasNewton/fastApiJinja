from pydantic import BaseModel
from enum import Enum



class Cond( str,Enum):
    Mint = "Mint"
    Good = "Good"
    Fair = "Fair"
    Poor = "Poor"
    Damaged = "Damaged"

class MatchBoxCar(BaseModel):
    Name: str
    Color: str
    Year: int
    State: Cond

