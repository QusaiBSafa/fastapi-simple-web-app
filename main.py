from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

class Item(BaseModel):
    id: int
    name: str

items = [Item(id=1, name='Item 1'), Item(id=2, name='Item 2')]

@app.get('/api/greet')
async def greet():
    return {'message': 'Hello, World!'}

@app.get('/api/items')
async def get_items():
    return items

@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})