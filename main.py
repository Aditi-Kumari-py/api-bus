from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

# Model to validate incoming location data
class LocationData(BaseModel):
    driverId: int
    latitude: float
    longitude: float
    timestamp: int  # Unix timestamp in milliseconds

received_data_log = []

@app.post("/receive-location")
async def receive_location(data: LocationData):
    readable_time = datetime.fromtimestamp(data.timestamp / 1000.0)
    log_entry = {
        "timestamp": readable_time.isoformat(),
        "driverId": data.driverId,
        "latitude": data.latitude,
        "longitude": data.longitude
    }
    received_data_log.append(log_entry)
    print("🛰️ Received:", log_entry)
    return {"status": "success"}

@app.get("/location-log")
async def get_logged_locations():
    return received_data_log
