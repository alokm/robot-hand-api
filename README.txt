This api provides the ability to monitor and control an anthropomorphic robotic human hand.


The api features:
- Separation of Concerns: The code is organized into different modules (api, models, services, utils) for better maintainability.
- Logging: Logging is implemented throughout the application using a custom logger setup.
- Aggregate API: An endpoint /hand/state is provided in sensor_data.py to retrieve the full state of the hand, including all joint positions, motor positions, motor forces, and tactile sensor states.
- Service Layer: HandService and SensorService classes handle the business logic, separating it from the API layer.
- Enhanced Models: The HandState and FingerState models are included to represent the full state of the hand.


To run this API:
- Install the required packages: fastapi, uvicorn, and pydantic. Using Pip or Pipenv (recommended)
- Navigate to the robotic_hand_api directory.
- Run the command: uvicorn main:app --reload

Copyright Alok Mohindra 2024 - All rights reserved