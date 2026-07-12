from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str

items = [Item(id=1, name='Item 1'), Item(id=2, name='Item 2')]

@router.get('/greet')
async def greet():
    return {'message': 'Hello, World!'}

@router.get('/items')
async def get_items():
    return items