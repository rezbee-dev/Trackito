from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/time")
async def get_time():
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }