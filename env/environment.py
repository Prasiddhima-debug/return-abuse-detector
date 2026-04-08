from env.models import Customer
from env.reward import calculate_reward

class ReturnEnv:
    def __init__(self, customers):
        self.customers = customers
        self.index = 0

    def reset(self):
        self.index = 0
        return self.state()

    def state(self):
        if self.index < len(self.customers):
            return self.customers[self.index]
        return None

    def step(self, action):
        customer = self.customers[self.index]

        # simple fraud logic
        is_fraud = customer.return_rate > 0.6

        reward = calculate_reward(action, is_fraud)

        self.index += 1
        done = self.index >= len(self.customers)

        return self.state(), reward, done, {}