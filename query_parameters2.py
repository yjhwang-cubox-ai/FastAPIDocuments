from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    
@app.get("/items2/")
async def read_items(q: Annotated[str|None, Query(min_length=3)]):
    results = {"items": [{"item_id":"Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results