import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from env.models import Customer  # sirf ek baar kaafi hai

def get_easy_task():
    return [
        Customer(
            customer_id=1,
            return_rate=0.8,
            account_age_days=30,
            total_orders=10,
            total_returns=8
        )
    ]