from typing import Annotated

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
    q: str | None = None
):
    results = {"item_id": item_id, "item": item}
    if q:
        results.update({"q": q})
    return results