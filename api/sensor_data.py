from fastapi import APIRouter, HTTPException
from services.sensor_service import SensorService
from utils.logger import get_logger

router = APIRouter()
sensor_service = SensorService()
logger = get_logger(__name__)


@router.get("/hand/tactile/{finger_id}")
async def get_tactile_sensor(finger_id: int):
    if finger_id not in range(1, 6):
        raise HTTPException(status_code=400, detail="Invalid finger ID")
    result = sensor_service.get_tactile_sensor(finger_id)
    logger.info(f"Retrieved tactile sensor data for finger {finger_id}")
    return result


@router.get("/hand/state")
async def get_hand_state():
    result = sensor_service.get_hand_state()
    logger.info("Retrieved full hand state")
    return result
