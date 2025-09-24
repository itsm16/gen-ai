from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field( # a function
        ..., # required
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Andrew"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000, # ge - greater than or equal to 100000
        le=100000
    )

class User(BaseModel):
    email: str = Field(..., regex=r"")