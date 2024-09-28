from pydantic import BaseModel, Field


class JointControl(BaseModel):
    position: float = Field(..., ge=-180, le=180)


class MotorControl(BaseModel):
    position: float = Field(..., ge=0, le=100)


class ForceControl(BaseModel):
    current: float = Field(..., ge=0, le=10)


class FingerControl(BaseModel):
    joint1: JointControl
    joint2: JointControl
    joint3: JointControl
    motor_position: MotorControl
    force: ForceControl


class HandControl(BaseModel):
    thumb: FingerControl
    index: FingerControl
    middle: FingerControl
    ring: FingerControl
    pinky: FingerControl


class FingerState(BaseModel):
    joint_positions: list[float]
    motor_position: float
    motor_force: float
    tactile_sensor: bool


class HandState(BaseModel):
    thumb: FingerState
    index: FingerState
    middle: FingerState
    ring: FingerState
    pinky: FingerState
