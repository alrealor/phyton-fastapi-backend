from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Allows main API having access to the resources of products API
router = APIRouter(prefix="/products", 
                   tags=["products"], 
                   responses={404: {"message":"resource not found"}})

# Product model
class Product(BaseModel):
    id: int
    name: str
    cost: float

products = [Product(id=1, name="Product 1", cost=123.987),
            Product(id=2, name="Product 1", cost=123.987),
           ]

# Get products operation
@router.get("/", response_model=list[Product])
async def get_products():
    return list(products)


# function to return a list of products by ID
def search_product(id: int):    
    productsById = filter(lambda item: item.id == id, products)
    try:
        return list(productsById)[0]
    except:
        return None
