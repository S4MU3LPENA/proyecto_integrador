from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: str
    username: str
    password: str

class UserCount(BaseModel):
    total: int