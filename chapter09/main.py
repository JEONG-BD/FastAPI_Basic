from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

FAKE_ITEM_DB = [{'item_name': 'Foo'},
                {'item_name': 'Bar'},
                {'item_name': 'Baz'}]


class FootEnum(str, Enum):
    fruit = 'fruit'
    vegetables = 'vegetables'
    dairy = 'dairy'


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# uvicorn main:app --reload

@app.get('/', description='This is our first route', tags=['Test'], deprecated=True)
async def root():
    return {'message':'hello world'}


@app.post('/', tags=['Test'], deprecated=False)
async def post():
    return {'message':'hello from post route'}


@app.put('/', tags=['Test'])
async def put():
    return {'message':'hello from put route'}


@app.get('/items', tags=['Item'])
async def list_items(skip: int = 0, limit: int = 10):
    return FAKE_ITEM_DB[skip:skip+limit]
    # return {'message':'list items route'}


@app.get('/items/{item_id}', tags=['Item'])
async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {'item_id': item_id}

    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {
                'description': 'Test Test Test Test'
            }
        )
        #return {'item_id': item_id, 'q':q}
    #return {'item_id': item_id}
    #return {'message':item_id}
    return item


@app.post('/items', tags=['Item'])
async def create_items(item: Item) -> Item:
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
        print(item_dict)
    return item_dict

@app.put('/items/{item_id}', tags=['Item'])
async def create_items(item_id: int, item: Item, q: str | None = None):
    result = {'item_id':item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result




@app.get('/users', tags=['User'])
async def list_users():
    return {'message':'list items route'}


@app.get('/users/current', tags=['User'])
async def get_current_user():
    return {'message':'this is the current user'}


@app.get('/users/{user_id}', tags=['User'])
async def get_user(user_id: str):
    return {'message':user_id}

@app.get('/foods/{food_name}', tags=['Food'])
async def get_food(food_name : FootEnum):
    if food_name == FootEnum.vegetables:
        return {'food_name': food_name, 'message': 'you are healthy'}

    if food_name.value == 'fruit':
        return {
            'food_name': food_name,
            'message': 'you are still healthy but like sweet things'
        }
    return {
        'food_name': food_name,
        'message': 'I like chocolate milk'
    }

