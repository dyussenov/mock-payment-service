from pydantic import BaseModel


class PaymentRequest(BaseModel):
    user_id: int
    event_id: int
    price: int
