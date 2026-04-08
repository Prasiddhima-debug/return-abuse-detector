from flask import Flask, jsonify, request
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

# RESET API (POST)
@app.route("/reset", methods=["POST"])
def reset():
    state = get_sample_state()
    return jsonify({
        "state": state
    })

# STEP API (POST)
@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action")  # integer expected (0,1,2)

    rewards = config.get("rewards", {})

    if action == 1:  # FLAG
        reward = rewards.get("correct_flag", 1.0)
    elif action == 0:  # APPROVE
        reward = rewards.get("missed_abuse", -1.0)
    else:  # INVESTIGATE
        reward = rewards.get("wrong_flag", -0.5)

    return jsonify({
        "state": get_sample_state(),
        "reward": reward,
        "done": True
    })

# VALIDATION CHECK
@app.route("/validate", methods=["GET"])
def validate():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
