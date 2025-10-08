from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def username_lenght(cls, v):
        if len(v) < 4:
            raise ValueError("should be atleast 4 chars")
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, vals):
        if vals.password != vals.confirm_password:
            raise ValueError("Password do not match")
        return vals