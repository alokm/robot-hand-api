from models.hand_models import HandState, FingerState


class SensorService:
    def get_tactile_sensor(self, hand_id: int, appendage: str):
        # Implementation to get tactile sensor values
        return {
            "hand_id": hand_id,
            "appendage": appendage,
            "tactile_value": False,
        }

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
