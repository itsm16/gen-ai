from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price:float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    # This is useful for fields that are computed from other fields, 
    # or for fields that are expensive to compute and should be cached.

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: int

    @computed_field
    @property
    def total(self) -> float:
        return self.nights * self.rate_per_night
    

bookingOne = Booking(user_id=1, room_id=201, nights=4, rate_per_night=2000)
print(bookingOne.total); # not total() since just a property now
print(bookingOne.model_dump()); # all about the class
