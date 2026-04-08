import random
from env.environment import ReturnEnv
from tasks.easy import get_easy_task

# 1️⃣ Load customers
customers = get_easy_task()

# 2️⃣ Create environment
env = ReturnEnv(customers)
print("Environment loaded successfully!")

# 3️⃣ Initialize Q-table (customer_id -> [action0, action1])
Q = {}
alpha = 0.5   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate

# 4️⃣ Training parameters
num_episodes = 10  # kitni baar poora customer list repeat kare
for episode in range(1, num_episodes + 1):
    state = env.reset()
    done = False
    print(f"\n--- Episode {episode} ---")
        
    while not done:
        customer_id = state.customer_id
        
        # Initialize Q-values if not present
        if customer_id not in Q:
            Q[customer_id] = [0, 0]
        
        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.choice([0, 1])  # explore
        else:
            action = 0 if Q[customer_id][0] > Q[customer_id][1] else 1  # exploit
        
        # Step through environment
        next_state, reward, done, _ = env.step(action)
        
        # Q-learning update
        if next_state is not None:
            next_id = next_state.customer_id
            if next_id not in Q:
                Q[next_id] = [0, 0]
            max_next = max(Q[next_id])
        else:
            max_next = 0
        
        Q[customer_id][action] = Q[customer_id][action] + alpha * (reward + gamma * max_next - Q[customer_id][action])
        
        # Print step (optional)
        print(f"Customer: {state}, Action: {action}, Reward: {reward}, Q-values: {Q[customer_id]}")
        
        state = next_state

# 5️⃣ Print final policy
print("\n✅ Training complete! Final policy (best action per customer):")
for cid, q_vals in Q.items():
    best_action = 0 if q_vals[0] > q_vals[1] else 1
    print(f"Customer {cid}: Best Action = {best_action}, Q-values = {q_vals}")