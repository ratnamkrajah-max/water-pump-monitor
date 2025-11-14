import random
import time
from datetime import datetime, timezone

import requests

API_URL = "http://localhost:8000/readings"
PUMPS = ["PUMP_A", "PUMP_B"]


def generate_reading(pump_id: str) -> dict:
    base_flow = 2.5
    base_pressure = 5.0

    flow = max(0.0, random.gauss(base_flow, 0.5))
    pressure = max(0.0, random.gauss(base_pressure, 1.0))

    status = "OK"
    if random.random() < 0.02:
        status = "FAULT"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pump_id": pump_id,
        "flow": flow,
        "pressure": pressure,
        "status": status,
    }


def main():
    while True:
        for pump_id in PUMPS:
            reading = generate_reading(pump_id)
            try:
                r = requests.post(API_URL, json=reading, timeout=5)
                r.raise_for_status()
                print(f"Sent reading for {pump_id}: {reading}")
            except Exception as e:
                print("Error posting reading:", e)
        time.sleep(5)


if __name__ == "__main__":
    main()
