from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)

# Load config
with open("openenv.yaml", "r") as f:
    config = yaml.safe_load(f)

# Simulate a transaction
def get_sample_state():
    return {
        "customer_id": 101,
        "return_reason": "damaged",
        "order_value": 1500,
        "return_count": 3,
        "days_since_purchase": 45
    }

@app.route("/reset", methods=["POST"])
def reset():
    state = get_sample_state()
    return jsonify({"state": state})

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action")
    
    valid_actions = config.get("actions", [])
    if action not in valid_actions:
        return jsonify({"error": "Invalid action"}), 400
    
    rewards = config.get("rewards", {})
    if action == "flag":
        reward = rewards.get("correct_flag", 1.0)
    elif action == "approve":
        reward = rewards.get("missed_abuse", -1.0)
    else:
        reward = rewards.get("wrong_flag", -0.5)
    
    return jsonify({
        "reward": reward,
        "done": True,
        "state": get_sample_state()
    })

@app.route("/validate", methods=["GET"])
def validate():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)