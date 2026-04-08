# inference.py

from env.environment import ReturnEnv
from tasks.easy import get_easy_task
# If you have medium/hard tasks, you can import them too
# from tasks.medium import get_medium_task
# from tasks.hard import get_hard_task

# Load customers for easy task (replace with medium/hard if needed)
customers = get_easy_task()

# Initialize environment
env = ReturnEnv(customers)

state = env.reset()
done = False
cumulative_reward = 0

# Start of portal-compliant inference
print("[START] Inference")

while not done:
    # Simple baseline: flag if return_rate > 0.6
    action = 1 if state.return_rate > 0.6 else 0
    
    # Step the environment
    next_state, reward, done, _ = env.step(action)
    
    # Update cumulative reward
    cumulative_reward += reward
    
    # Portal-compliant structured log
    print(f"[STEP] CustomerID={state.customer_id} Action={action} Reward={reward} Cumulative={cumulative_reward}")
    
    # Move to next state
    state = next_state

# End of inference
print("[END] Inference ✅")