from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str
    price: int

#GET
@app.get("/items")
def get_items():
    return items

# POST
@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return item

# PUT
@app.put("/items/{item_id}")
def update_item(item_i: int, updated_item: Item):
    if item_i < len(items):
        items[item_i] = updated_item.dict()
        return updated_item
    return {"error": "Item not found"}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_i: int):
    if item_i < len(items):
        deleted_item = items.pop(item_i)
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "Item not found"}
