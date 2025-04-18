from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="FastAPI Swagger Demo",
    description="A standalone FastAPI app showcasing Swagger UI with API endpoints.",
    version="1.0.0",
    docs_url="/docs"
)

# Pydantic model for request/response
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

# Redirect root to Swagger UI
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    Redirects the root URL to the Swagger UI.
    """
    # return RedirectResponse(url="/docs")
    return RedirectResponse(url="/rapidoc")

@app.get("/items/", response_model=List[Item], tags=["Items"])
async def get_items(min_price: Optional[float] = None, max_price: Optional[float] = None):
    """
    Retrieves a list of items, filtered by optional min_price and max_price query parameters.
    """
    items = [
        {"name": "Laptop", "price": 999.99, "description": "High-performance laptop"},
        {"name": "Phone", "price": 499.99, "description": "Latest smartphone"},
        {"name": "Headphones", "price": 79.99, "description": "Wireless headphones"}
    ]
    filtered_items = items
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] >= min_price]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] <= max_price]
    return filtered_items

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def get_item(item_id: int):
    """
    Retrieves a single item by ID. Raises 404 if not found.
    """
    items = {
        1: {"name": "Laptop", "price": 999.99, "description": "High-performance laptop"},
        2: {"name": "Phone", "price": 499.99, "description": "Latest smartphone"}
    }
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/", response_model=Item, tags=["Items"])
async def create_item(item: Item):
    """
    Creates a new item with name, price, and optional description.
    """
    return item

# Serve dark theme RapiDoc
@app.get("/rapidoc", include_in_schema=False, response_class=HTMLResponse)
async def rapidoc():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
      </head>
      <body>
        <rapi-doc spec-url=\"{0}\" theme=\"dark\"></rapi-doc>
      </body>
    </html>
    """.format(app.openapi_url)
