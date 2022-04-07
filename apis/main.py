from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI
from databases import Database

import time

app = FastAPI()
database = Database("sqlite:///db.db")


class SensorReading(BaseModel):
    name: str
    value: float
    time: Optional[float] = time.time()

@app.on_event("startup")
async def open_database():
    await database.connect()

@app.on_event("shutdown")
async def close_database():
    await database.disconnect()

@app.get("/")
def read_root():
    return [{"Hello": "World"}]

@app.get("/readings")
async def read_readings():
    return await database.fetch_all("SELECT * FROM sensor_readings")

@app.get("/readings/{sensor_name}")
async def read_reading(sensor_name: str):
    return await database.fetch_all("SELECT * FROM sensor_readings WHERE name = :name",
    {"name":sensor_name})

@app.put("/readings")
async def put_reading(reading: SensorReading):
    return await database.execute(
        "INSERT INTO sensor_readings (name,value,time) VALUES (:name,:value,:time)",
        {"name": reading.name, "value":reading.value, "time": reading.time})
