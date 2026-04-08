from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Load config
with open("openenv.yaml", "r") as f:
    config = yaml.safe_load(f)

def get_sample_state():
    return {
        "customer_id": 101,
        "return_reason": "damaged",
        "order_value": 1500,
        "return_count": 3,
        "days_since_purchase": 45
    }

# RESET (IMPORTANT FIX)
@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({
        "state": get_sample_state(),
        "info": {}
    }), 200

# STEP (IMPORTANT FIX)
@app.route("/step", methods=["POST"])
def step():
    data = request.get_json(force=True)
    action = data.get("action", 0)

    rewards = config.get("rewards", {})

    if action == 1:
        reward = rewards.get("correct_flag", 1.0)
    elif action == 0:
        reward = rewards.get("missed_abuse", -1.0)
    else:
        reward = rewards.get("wrong_flag", -0.5)

    return jsonify({
        "state": get_sample_state(),
        "reward": reward,
        "done": True,
        "info": {}
    }), 200

# HEALTH CHECK
@app.route("/", methods=["GET"])
def home():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
