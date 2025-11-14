from typing import List

from fastapi import FastAPI, HTTPException

from .models import SensorReading, Alert
from .alerts import evaluate_alerts
from . import storage

app = FastAPI(title="Water Pump Monitor API")


@app.get("/")
def root():
    return {"message": "Water Pump Monitor API is running"}


@app.post("/readings", response_model=List[Alert])
def ingest_reading(reading: SensorReading):
    """
    Ingest a new sensor reading, evaluate alerts,
    and store both the reading and any alerts generated.
    """
    alerts = evaluate_alerts(reading)
    storage.add_reading(reading, alerts)
    return alerts


@app.get("/readings/latest")
def get_latest_all():
    """
    Get the latest reading for each pump.
    """
    return storage.get_all_latest_readings()


@app.get("/readings/latest/{pump_id}", response_model=SensorReading)
def get_latest_for_pump(pump_id: str):
    """
    Get the latest reading for a specific pump.
    """
    reading = storage.get_latest_reading(pump_id)
    if reading is None:
        raise HTTPException(status_code=404, detail="Pump not found")
    return reading


@app.get("/alerts", response_model=List[Alert])
def list_alerts(limit: int = 100):
    """
    Get recent alerts, up to the specified limit.
    """
    return storage.get_recent_alerts(limit=limit)
