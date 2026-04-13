from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items = [
    Item(id=1, name="Notebook", description="A blank notebook.", price=3.99),
    Item(id=2, name="Pencil", description="A graphite pencil.", price=0.99),
]

@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")

# Run with: uvicorn starter-code:app --reload
