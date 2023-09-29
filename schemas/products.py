from typing import Optional
from pydantic import BaseModel

class product(BaseModel):
    id: Optional[int]
    name: str
    price: str
    Stock: str
    category: str

class categories(BaseModel):
    id: Optional[int]
    name: str
    