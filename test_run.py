from env.environment import ReturnEnv
from tasks.easy import get_easy_task
import random

# 1️⃣ Load customers
customers = get_easy_task()

# 2️⃣ Create environment
env = ReturnEnv(customers)
print("Environment loaded successfully!")

# 3️⃣ Reset environment (get first state)
state = env.reset()
done = False

# 4️⃣ Process all customers
while not done:
    print("Customer:", state)

    # Random action: 0 = no flag, 1 = flag
    action = random.choice([0, 1])

    # Step through environment
    state, reward, done, _ = env.step(action)

    print("Action taken:", action)
    print("Reward:", reward)
    print("------")

print("All customers processed! ✅")