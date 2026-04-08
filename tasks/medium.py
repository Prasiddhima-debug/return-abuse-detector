from env.models import Customer

def get_medium_task():
    return [
        Customer(1, 0.7, 20, 15, 10),   # fraud
        Customer(2, 0.2, 200, 50, 5),   # genuine
        Customer(3, 0.5, 100, 30, 15),  # medium
        Customer(4, 0.8, 10, 8, 7),     # fraud
        Customer(5, 0.1, 300, 100, 2)   # genuine
    ]
