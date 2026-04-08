from env.environment import ReturnEnv
from tasks.easy import get_easy_task

customers = get_easy_task()
env = ReturnEnv(customers)

state = env.reset()
done = False

while not done:
    # simple baseline: always flag if return_rate > 0.6
    action = 1 if state.return_rate > 0.6 else 0
    state, reward, done, _ = env.step(action)
    print(f"Customer {state.customer_id if state else 'done'}: Action={action}, Reward={reward}")