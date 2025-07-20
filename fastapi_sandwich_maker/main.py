from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Food(BaseModel):
    id: int
    name: str
    price: float

food_instance = [
    Food(id=1, name="Ham Sandwich", price=5.99),
    Food(id=2, name="Veggie Sandwich", price=4.99)
]

@app.get("/")
def read_all():
    return food_instance

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return next((item for item in food_instance if item.id == item_id), {})

@app.post("/items")
def add_item(food: Food):
    food_instance.append(food)
    return food

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global food_instance
    food_instance = [item for item in food_instance if item.id != item_id]
    return food_instance

@app.put("/items/{item_id}/name")
def update_item_name(item_id: int, new_name: str):
    for item in food_instance:
        if item.id == item_id:
            item.name = new_name
            return item
    return {"error": "Item not found"}

