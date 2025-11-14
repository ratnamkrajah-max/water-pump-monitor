from typing import List
from .models import SensorReading, Alert

# Thresholds can be adjusted later or moved to a config file
HIGH_PRESSURE_THRESHOLD = 8.0    # bar
LOW_FLOW_THRESHOLD = 1.0         # m3/s


def evaluate_alerts(reading: SensorReading) -> List[Alert]:
    alerts: List[Alert] = []

    if reading.pressure > HIGH_PRESSURE_THRESHOLD:
        alerts.append(
            Alert(
                pump_id=reading.pump_id,
                level="critical",
                message=f"High pressure: {reading.pressure} bar"
            )
        )

    if reading.flow < LOW_FLOW_THRESHOLD:
        alerts.append(
            Alert(
                pump_id=reading.pump_id,
                level="warning",
                message=f"Low flow: {reading.flow} m3/s"
            )
        )

    if reading.status != "OK":
        alerts.append(
            Alert(
                pump_id=reading.pump_id,
                level="warning",
                message=f"Pump status: {reading.status}"
            )
        )

    return alerts
