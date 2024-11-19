from fastapi import FastAPI
import os
from dotenv import load_dotenv
import json
from uuid import uuid4
from datetime import datetime
from fastapi import HTTPException
from models import Thread, Product
from base_models import ProductItem, UpdateProductItem


app = FastAPI()

# Load .env file
load_dotenv()

# DB_URL = os.getenv("DB_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")
# DEBUG = os.getenv("DEBUG") == "True"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def add_products(item: ProductItem):
    """Add a new product"""
    print(item)
    item_data = item.model_dump(exclude_unset=True)
    item_data["id"] = str(uuid4())
    new_prod = Product(**item_data).save()
    return {"item": new_prod}


@app.get("/items")
def get_thread_items():
    """
    Get all products in the DB
    """
    items = Product.scan()
    print(items)
    return {"items": items}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    """
    Read a single product by ID
    """
    item = Product.get(item_id)
    if item:
        return {"item": item.attribute_values}
    else:
        return {"detail": "Product not found"}


@app.put("/items/{item_id}")
def update_product(update_data: UpdateProductItem, item_id: str):
    """
    Update a single product
    """
    try:
        # Fetch the existing item
        item = Product.get(item_id)

        # Update fields only if provided in the update_data
        for key, value in update_data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        # Update the updated_at field
        item.updated_at = datetime.now()

        # Save the updated item to the database
        item.save()

        return {"item": item.attribute_values}
    except Product.DoesNotExist:
        raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/items/{item_id}")
def delete_itme(item_id: str):
    """
    Delete a single product by ID
    """
    item = Product.get(item_id)
    if item:
        item.delete()
        return {"detail": "Item deleted successfully"}
    else:
        return {"detail": "Product not found"}
