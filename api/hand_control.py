from fastapi import APIRouter, HTTPException
from models.hand_models import JointControl, MotorControl, ForceControl, HandControl
from services.hand_service import HandService
from utils.logger import get_logger

router = APIRouter()
hand_service = HandService()
logger = get_logger(__name__)


@router.post("/hand/joint/{finger_id}/{joint_id}")
async def set_joint_position(finger_id: int, joint_id: int, control: JointControl):
    if finger_id not in range(1, 6) or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid finger or joint ID")
    result = hand_service.set_joint_position(finger_id, joint_id, control.position)
    logger.info(
        f"Set joint position: finger {finger_id}, joint {joint_id}, position {control.position}"
    )
    return result


@router.post("/hand/motor/{finger_id}/{joint_id}")
async def set_motor_position(finger_id: int, joint_id: int, control: MotorControl):
    if finger_id not in range(1, 6) or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid finger or joint ID")
    result = hand_service.set_motor_position(finger_id, joint_id, control.position)
    logger.info(
        f"Set motor position: finger {finger_id}, joint {joint_id}, position {control.position}"
    )
    return result


@router.post("/hand/force/{finger_id}/{joint_id}")
async def set_motor_current(finger_id: int, joint_id: int, control: ForceControl):
    if finger_id not in range(1, 6) or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid finger or joint ID")
    result = hand_service.set_motor_current(finger_id, joint_id, control.current)
    logger.info(
        f"Set motor current: finger {finger_id}, joint {joint_id}, current {control.current}"
    )
    return result


@router.post("/hand/control")
async def control_hand(hand_data: HandControl):
    result = hand_service.control_hand(hand_data)
    logger.info("Updated full hand configuration")
    return result
