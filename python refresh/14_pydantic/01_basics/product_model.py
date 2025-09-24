from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# print(type("True")) # <class 'str'>
print(type("35.00")) # <class 'str'>
# print(type(35.00)) # <class 'float'>

penRey = Product(id=1, name="Trimax", price="35.00", in_stock="True")

# penCello = Product(name="Freeflo")
# required error

#default conversions
# "35.0" str to int , "True" (str) to int 

print(penRey); # id=1 name='Trimax' price=35.0 in_stock=True


