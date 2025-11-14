from collections import defaultdict
from typing import Dict, List

from .models import SensorReading, Alert

# In-memory store:
# - readings grouped by pump_id
# - a simple list of alerts
_readings_by_pump: Dict[str, List[SensorReading]] = defaultdict(list)
_alerts: List[Alert] = []


def add_reading(reading: SensorReading, alerts: List[Alert]) -> None:
    readings = _readings_by_pump[reading.pump_id]
    readings.append(reading)

    # Keep history to a reasonable size (can be tuned later)
    max_history = 10_000
    if len(readings) > max_history:
        # drop oldest entries
        del readings[0 : len(readings) - max_history]

    _alerts.extend(alerts)


def get_latest_reading(pump_id: str) -> SensorReading | None:
    readings = _readings_by_pump.get(pump_id)
    if not readings:
        return None
    return readings[-1]


def get_all_latest_readings() -> Dict[str, SensorReading]:
    return {pump_id: readings[-1] for pump_id, readings in _readings_by_pump.items()}


def get_recent_alerts(limit: int = 100) -> List[Alert]:
    return _alerts[-limit:]
