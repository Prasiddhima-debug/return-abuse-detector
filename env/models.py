from pydantic import BaseModel

class Customer(BaseModel):
    customer_id: int
    return_rate: float   # 0 to 1
    account_age_days: int
    total_orders: int
    total_returns: int

    def is_high_risk(self):
        return self.return_rate > 0.6