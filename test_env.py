# Dummy customers list for testing
customers = ["customer1", "customer2", "customer3"]

from env.environment import ReturnEnv

# Environment object banao
env = ReturnEnv(customers)
print("Environment loaded successfully!")

# Environment reset aur initial state
state = env.reset()
print("Initial state:", state)

print("Environment basic test complete!")