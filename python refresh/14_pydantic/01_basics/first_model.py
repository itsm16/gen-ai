from pydantic import BaseModel

# pydantic is used for validation

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data_one = {
    "id": 1,
    "name": "Andrew",
    "is_active": True
}
# no error from this

input_data_two = {
    "id": 2,
    "name": "Andy",
    "is_active": 25 # is_active should be a bool
}
# input_data_two will give validation error 

userOne = User(**input_data_one) # unpack values
userTwo = User(**input_data_two)

# print(userOne) # id=1 name='Andrew' is_active=True
print(userTwo)

