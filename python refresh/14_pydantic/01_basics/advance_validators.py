from pydantic import BaseModel, field_validator

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_in_capital(cls, v):
        if not v.istitle():
            raise ValueError("Name in capital")
        return v

class User(BaseModel):
    email: str

    @field_validator("email")
    def normalized(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price: str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v
    
productOne = Product(price="4.44")
print(productOne.parse_price)