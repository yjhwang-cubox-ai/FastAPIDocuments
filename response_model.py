from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    
@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item