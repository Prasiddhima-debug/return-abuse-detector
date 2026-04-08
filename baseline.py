from env.environment import ReturnEnv
from tasks.easy import get_easy_task

def simple_agent(customer):
    # basic rule based decision
    if customer.return_rate > 0.6:
        return 1  # FLAG
    elif customer.return_rate > 0.3:
        return 2  # INVESTIGATE
    else:
        return 0  # APPROVE

# load task
customers = get_easy_task()

# create env
env = ReturnEnv(customers)

state = env.reset()
done = False
total_reward = 0

while not done:
    action = simple_agent(state)
    state, reward, done, _ = env.step(action)
    total_reward += reward

print("Total Reward:", total_reward)