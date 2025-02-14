from pydantic import BaseModel

class Machine(BaseModel):
    name: str
    temperature: float
    pressure: float
    vibration: float
    efficiency: float
