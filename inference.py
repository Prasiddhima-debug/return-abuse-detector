from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ActionInput(BaseModel):
    action: int

# STATIC OBSERVATION
def obs():
    return {
        "customer_id": 1,
        "return_rate": 0.5,
        "account_age_days": 100,
        "total_orders": 20,
        "total_returns": 5
    }

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return {
        "observation": obs()
    }

@app.post("/step")
def step(input_data: ActionInput):
    return {
        "observation": obs(),
        "reward": 1.0,
        "done": True
    }
