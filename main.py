from fastapi import FastAPI
from api import hand_control, sensor_data
from utils.logger import setup_logger

app = FastAPI()

# Setup logging
logger = setup_logger()

# Include routers
app.include_router(hand_control.router)
app.include_router(sensor_data.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
