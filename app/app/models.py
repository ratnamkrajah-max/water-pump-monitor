from datetime import datetime
from pydantic import BaseModel, Field


class SensorReading(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    pump_id: str
    flow: float
    pressure: float
    status: str


class Alert(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    pump_id: str
    level: str
    message: str
