from fastapi import APIRouter, HTTPException
from services.sensor_service import SensorService
from utils.logger import get_logger

router = APIRouter()
sensor_service = SensorService()
logger = get_logger(__name__)


# -------fix below-------
@router.get("v0/hand/tactile/{hand_id}/{appendage}/{joint_id}")
async def get_tactile_sensor(hand_id, appendage: str):
    if appendage not in [
        "wrist",
        "thumb",
        "index",
        "middle",
        "ring",
        "pinky",
    ]:
        raise HTTPException(status_code=400, detail="Invalid appendage")
    result = sensor_service.get_tactile_sensor(appendage)
    logger.info(f"Retrieved tactile sensor data for appendage {appendage}")
    return result


@router.get("v0/hand/state")
async def get_hand_state():
    result = sensor_service.get_hand_state()
    logger.info("Retrieved full hand state")
    return result
