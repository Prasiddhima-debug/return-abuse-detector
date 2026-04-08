from fastapi import FastAPI
from pydantic import BaseModel
import yaml

app = FastAPI()

# Load config
with open("openenv.yaml", "r") as f:
    config = yaml.safe_load(f)

class ActionInput(BaseModel):
    action: int

def get_sample_state():
    return {
        "customer_id": 101,
        "return_reason": "damaged",
        "order_value": 1500,
        "return_count": 3,
        "days_since_purchase": 45
    }

# RESET
@app.post("/reset")
def reset():
    return {
        "state": get_sample_state(),
        "info": {}
    }

# STEP
@app.post("/step")
def step(input_data: ActionInput):
    action = input_data.action
    rewards = config.get("rewards", {})

    if action == 1:
        reward = rewards.get("correct_flag", 1.0)
    elif action == 0:
        reward = rewards.get("missed_abuse", -1.0)
    else:
        reward = rewards.get("wrong_flag", -0.5)

    return {
        "state": get_sample_state(),
        "reward": reward,
        "done": True,
        "info": {}
    }

# HEALTH
@app.get("/")
def home():
    return {"status": "ok"}
