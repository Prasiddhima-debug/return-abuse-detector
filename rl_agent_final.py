import random
import csv
from env.environment import ReturnEnv
from tasks.easy import get_easy_task

# 1️⃣ Load customers
customers = get_easy_task()

# 2️⃣ Create environment
env = ReturnEnv(customers)
print("Environment ready! Let's train 🚀")

# 3️⃣ Q-table init
Q = {}  # customer_id -> [action0, action1]
alpha = 0.5   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration

# 4️⃣ Training setup
episodes = 100
for ep in range(1, episodes+1):
    state = env.reset()
    done = False

    while not done:
        cid = state.customer_id

        # Q-values init if new customer
        if cid not in Q:
            Q[cid] = [0, 0]

        # 5️⃣ Pick action (epsilon-greedy)
        if random.random() < epsilon:
            action = random.choice([0,1])
        else:
            action = 0 if Q[cid][0] > Q[cid][1] else 1

        # 6️⃣ Take action
        next_state, reward, done, _ = env.step(action)

        # 7️⃣ Update Q
        if next_state:
            next_cid = next_state.customer_id
            if next_cid not in Q:
                Q[next_cid] = [0,0]
            max_next = max(Q[next_cid])
        else:
            max_next = 0

        Q[cid][action] += alpha * (reward + gamma*max_next - Q[cid][action])

        state = next_state

    # 8️⃣ Progress print every 10 episodes
    if ep % 10 == 0:
        print(f"Episode {ep}/{episodes} done ✅")

# 9️⃣ Show final policy
print("\nTraining finished! Here's the final policy:")
for cid, q_vals in Q.items():
    best = 0 if q_vals[0] > q_vals[1] else 1
    print(f"Customer {cid}: Best Action = {best}, Q = {q_vals}")

# 10️⃣ Save policy
with open("final_policy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id","best_action","Q0","Q1"])
    for cid, q_vals in Q.items():
        best = 0 if q_vals[0] > q_vals[1] else 1
        writer.writerow([cid,best,q_vals[0],q_vals[1]])

print("\nSaved final_policy.csv 📁")