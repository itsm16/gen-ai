from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class Blogpost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

cart_data = {
    "user_id": 223,
    "items": ["Laptop", "Tab"],
    "quantities": {"laptop":1, "tab":1}
}

cart = Cart(**cart_data);
print(cart) # user_id=223 items=['Laptop', 'Tab'] quantities={'laptop': 1, 'tab': 1}


