import random
from env.environment import ReturnEnv
from tasks.easy import get_easy_task

# 1️⃣ Load customers
customers = get_easy_task()

# 2️⃣ Create environment
env = ReturnEnv(customers)
print("Environment loaded successfully!")

# 3️⃣ Initialize Q-table (customer_id -> action -> value)
# Simple dict for demonstration
Q = {}  # key: customer_id, value: [Q-value for action 0, Q-value for action 1]

alpha = 0.5   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate

# 4️⃣ Reset environment
state = env.reset()
done = False

while not done:
    customer_id = state.customer_id  # unique id for Q-table
    
    # Initialize Q-values if not present
    if customer_id not in Q:
        Q[customer_id] = [0, 0]  # [action 0, action 1]
    
    # 5️⃣ Choose action (epsilon-greedy)
    if random.random() < epsilon:
        action = random.choice([0, 1])  # explore
    else:
        action = 0 if Q[customer_id][0] > Q[customer_id][1] else 1  # exploit
    
    # 6️⃣ Take action in environment
    next_state, reward, done, _ = env.step(action)
    
    # 7️⃣ Q-learning update
    if next_state is not None:
        next_id = next_state.customer_id
        if next_id not in Q:
            Q[next_id] = [0, 0]
        max_next = max(Q[next_id])
    else:
        max_next = 0
    
    # Update Q-value for current state-action
    Q[customer_id][action] = Q[customer_id][action] + alpha * (reward + gamma * max_next - Q[customer_id][action])
    
    # 8️⃣ Print step
    print("Customer:", state)
    print("Action taken:", action)
    print("Reward:", reward)
    print("Updated Q-values:", Q[customer_id])
    print("------")
    
    # Move to next state
    state = next_state

print("All customers processed! ✅")