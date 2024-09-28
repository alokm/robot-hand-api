from fastapi import APIRouter, HTTPException
from models.hand_models import JointControl, MotorControl, ForceControl, HandControl
from services.hand_service import HandService
from utils.logger import get_logger

router = APIRouter()
hand_service = HandService()
logger = get_logger(__name__)


# Labels for hands, parts of hand and movements
# hand_id: unique id for hand
# appendage: wrist, thumb, index, middle, ring, pinky
# movement: rotate (wrist only), lateral, transverse
# setting: float - positive or negative

# TODO: Implement position, motor and force code


@router.post("v0/hand/position/{hand_id}/{appendage}/{joint_id}")
async def set_joint_position(
    hand_id, appendage: str, joint_id: int, control: JointControl
):
    if appendage not in [
        "wrist",
        "thumb",
        "index",
        "middle",
        "ring",
        "pinky",
    ] or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid appendage or joint ID")
    result = hand_service.set_joint_position(appendage, joint_id, control.position)
    logger.info(
        f"Set joint position on {hand_id}: {appendage}, joint {joint_id}, position {control.position}"
    )
    return result


@router.post("v0/hand/motor/{hand_id}/{appendage}/{joint_id}")
async def set_motor_position(
    hand_id, appendage: str, joint_id: int, control: MotorControl
):
    if appendage not in [
        "wrist",
        "thumb",
        "index",
        "middle",
        "ring",
        "pinky",
    ] or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid appendage or joint ID")
    result = hand_service.set_motor_position(appendage, joint_id, control.position)
    logger.info(
        f"Set motor position on {hand_id}: {appendage}, joint {joint_id}, position {control.position}"
    )
    return result


@router.post("/v0/hand/force/{hand_id}/{appendage}/{joint_id}")
async def set_motor_current(
    hand_id, appendage: str, joint_id: int, control: ForceControl
):
    if appendage not in [
        "wrist",
        "thumb",
        "index",
        "middle",
        "ring",
        "pinky",
    ] or joint_id not in range(1, 4):
        raise HTTPException(status_code=400, detail="Invalid appendage or joint ID")
    result = hand_service.set_motor_current(appendage, joint_id, control.current)
    logger.info(
        f"Set motor current on {hand_id}: {appendage}, joint {joint_id}, current {control.current}"
    )
    return result


@router.post("/hand/control")
async def control_hand(hand_data: HandControl):
    result = hand_service.control_hand(hand_data)
    logger.info("Updated full hand configuration")
    return result
