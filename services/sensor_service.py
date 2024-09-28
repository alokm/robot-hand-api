from models.hand_models import HandState, FingerState


class SensorService:
    def get_tactile_sensor(self, finger_id: int):
        # Implementation to get tactile sensor values
        return {"finger_id": finger_id, "tactile_value": True}  # Example binary value

    def get_hand_state(self) -> HandState:
        # Implementation to get the full hand state
        return HandState(
            thumb=FingerState(
                joint_positions=[0, 0, 0],
                motor_position=0,
                motor_force=0,
                tactile_sensor=False,
            ),
            index=FingerState(
                joint_positions=[0, 0, 0],
                motor_position=0,
                motor_force=0,
                tactile_sensor=False,
            ),
            middle=FingerState(
                joint_positions=[0, 0, 0],
                motor_position=0,
                motor_force=0,
                tactile_sensor=False,
            ),
            ring=FingerState(
                joint_positions=[0, 0, 0],
                motor_position=0,
                motor_force=0,
                tactile_sensor=False,
            ),
            pinky=FingerState(
                joint_positions=[0, 0, 0],
                motor_position=0,
                motor_force=0,
                tactile_sensor=False,
            ),
        )
