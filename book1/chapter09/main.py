from enum import Enum
from typing import Optional, Literal, Union
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import FastAPI, Query, Path, Body, Cookie, Header, File, Form, Header, status
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import List

app = FastAPI()

# FAKE_ITEM_DB = [{'item_name': 'Foo'},
#                 {'item_name': 'Bar'},
#                 {'item_name': 'Baz'}]
#
#
# class FootEnum(str, Enum):
#     fruit = 'fruit'
#     vegetables = 'vegetables'
#     dairy = 'dairy'
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
# # uvicorn main:app --reload
#
# @app.get('/', description='This is our first route', tags=['Test'], deprecated=True)
# async def root():
#     return {'message':'hello world'}
#
#
# @app.post('/', tags=['Test'], deprecated=False)
# async def post():
#     return {'message':'hello from post route'}
#
#
# @app.put('/', tags=['Test'])
# async def put():
#     return {'message':'hello from put route'}
#
#
# #@app.get('/items', tags=['Item'])
# #async def list_items(skip: int = 0, limit: int = 10):
#     #return FAKE_ITEM_DB[skip:skip+limit]
#     #return {'message':'list items route'}
#
#
# @app.get('/items/{item_id}', tags=['Item'])
# async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {'item_id': item_id}
#
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {
#                 'description': 'Test Test Test Test'
#             }
#         )
#         #return {'item_id': item_id, 'q':q}
#     #return {'item_id': item_id}
#     #return {'message':item_id}
#     return item
#
#
# @app.post('/items', tags=['Item'])
# async def create_items(item: Item) -> Item:
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price_with_tax': price_with_tax})
#         print(item_dict)
#     return item_dict
#
# @app.put('/items/{item_id}', tags=['Item'])
# async def create_items(item_id: int, item: Item, q: str | None = None):
#     result = {'item_id':item_id, **item.dict()}
#     if q:
#         result.update({'q': q})
#     return result
#
#
# @app.get('/items', tags=['Item'])
# async def read_items(remark: str | None = Query(..., min_length=3, max_length=10, description='This is a sample query string', alias='item-query')):
#     result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if remark:
#         result.update({'remark': remark})
#     return result
#
#
# @app.get('/items_hidden', tags=['Item'])
# async def hidden_items(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {'hidden_query': hidden_query}
#     return {'hidden_query': 'Not found'}
#
#
# @app.get('/items_validation/{item_id}', tags=['Item'])
# async def read_item_validation(
#         *,
#         item_id: int = Path(..., title='The ID of the item to get', ge=10, le=100),
#         q: str | None = Query(None, alias='item-query'), size: float = Query(..., gt=0, lt=7.75)):
#
#     result = {'item_id': item_id, 'size': size}
#
#     if q:
#         result.update({'q': q})
#     return result
#
#
# @app.get('/users', tags=['User'])
# async def list_users():
#     return {'message':'list items route'}
#
#
# @app.get('/users/current', tags=['User'])
# async def get_current_user():
#     return {'message':'this is the current user'}
#
#
# @app.get('/users/{user_id}', tags=['User'])
# async def get_user(user_id: str):
#     return {'message':user_id}
#
#
# @app.get('/foods/{food_name}', tags=['Food'])
# async def get_food(food_name : FootEnum):
#     if food_name == FootEnum.vegetables:
#         return {'food_name': food_name, 'message': 'you are healthy'}
#
#     if food_name.value == 'fruit':
#         return {
#             'food_name': food_name,
#             'message': 'you are still healthy but like sweet things'
#         }
#     return {
#         'food_name': food_name,
#         'message': 'I like chocolate milk'
#     }
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     firstname: str
#     lastname: str | None = None
#
#
# class Importance(BaseModel):
#     importance: int
#
# @app.put('/items/{item_id}')
# async def item(*,
#                item_id: int = Path(..., title='The Id of the item to get', ge=0, le=150),
#                q: str | None = None,
#                item: Item | None = None,
#                user: User,
#                importance: int = Body(..., embed=True)):
#
#     result = {'item_id':item_id}
#     if q:
#         result.update({'q': q})
#     if item:
#         result.update({'item': item})
#     if user:
#         result.update({'user': user})
#     if importance:
#         result.update({'importance':importance})
#     return result

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(title='The Description of the item', max_length=300)
#     price: float = Field(..., gt=0, description='The price must be greater than zero')
#
#
# @app.put('/items/{item_id}', tags=['Item'])
# async def update_item(item_id : int, item: Item = Body(..., embed=True)):
#     result = {'item_id': item_id, 'item': item}
#     return result

#
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     # tags: list[str] = []
#     tags: set[str] = []
#     image: list[Image] | None = None
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]
#
#
# @app.put('/item/{item_id}', tags=['Item'])
# async def update_item(item_id: int, item: Item):
#     result = {'item_id': item_id, 'item': item}
#     return result
#
#
# @app.post('/offers', tags=['ETC'])
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
#
# @app.post('/images/multiple', tags=['ETC'])
# async def create_multiple_images(images: list[Image]):
#     return images

# class Item(BaseModel):
#     name: str
#     description: str | None
#     price: float
#     tax: float | None

    # name: str = Field(..., example='Foo')
    # description: str | None = Field(..., example='A very nice Item')
    # price: float = Field(..., example=16.25)
    # tax: float | None = Field(..., example=1.67)

    # class Config :
    #     schema_extra = {
    #         'example': {
    #             'name': 'Foo',
    #             'description': 'A very nice Item',
    #             'price': 16.25,
    #             'tax': 1.67
    #         }
    #     }

# @app.put('/item/{item_id}', tags=['Item'])
# async def update_item(
#         item_id: int,
#         item: Item = Body(
#             ...,
#             openapi_examples={
#                 'normal': {
#                     'name': 'Foo',
#                     'description': 'A very nice Item',
#                     'price': 16.25,
#                     'tax': 1.67
#                 },
#                 'converted': {
#                     'summary': 'Amn example with converted data',
#                     'description': 'FastAPI can convert price `string` to actual `numbers` automatic',
#                     'value': {'name': 'Bar', 'price': '16.25'}
#                 },
#                 'invalid': {
#                     'summary': 'Invalid data is rejected with an error',
#                     'value': {'name': 'Baz', 'price': 'sixteen point two five'}
#                 }
#             }
#         )
#     ):
#     result = {'item_id': item_id, 'item': item}
#     return result

# @app.put('/items/{item_id}')
# async def read_items(item_id: UUID,
#                      start_date: datetime | None = Body(None),
#                      end_date: datetime | None = Body(None),
#                         repeat_at: time | None = Body(None),
#                         process_after : timedelta | None = Body(None),
#                      ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {'item_id': item_id,
#             'start_date': start_date,
#             'end_date': end_date,
#             'repeat_at': repeat_at,
#             'process_after': process_after,
#             'start_process': start_process,
#             'duration': duration
#             }

#
# @app.get('/items')
# async def read_itmes(
#         cookie_id: str | None = Cookie(None),
#         accept_encoding: str | None = Header(None, convert_underscores=False),
#         sec_ch_ua: str | None = Header(None),
#         user_agent: str | None = Header(None),
#         x_token: list[str] | None = Header(None),
# ):
#     return {
#         'cookie_id': cookie_id,
#         'Accept-Encoding': accept_encoding,
#         'sec-ch-ua': sec_ch_ua,
#         'User-Agent': user_agent,
#         'X-token values': x_token
#     }
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []
#
# items = {
#     'foo': {'name': 'Foo', 'price': 50.2},
#     'bar': {'name': 'Bar', 'desciption': 'The bartenders', 'price': 62, 'tax': 20.2},
#     'baz': {'name': 'Baz', 'desciption': None, 'price': 50.2, 'tax': 10.5, 'tags':[]}
# }
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None
#
# class UserOut(UserBase):
#     pass
#
#
# @app.post('/items/', response_model=Item, tags=['Items'])
# async def create_item(item: Item):
#     return item
#
#
# @app.get('/items/{items_id}',
#          response_model=Item,
#          response_model_exclude_unset=True,
#          tags=['Items'])
# async def read_item(item_id: Literal['foo', 'bar', 'baz']):
#     return items[item_id]
#
#
# @app.get('/items/{items_id}/name',
#          response_model=Item,
#          response_model_include=['name', 'description'],
#          tags=['Items'])
# async def read_item_name(item_id: Literal['foo', 'bar', 'baz']):
#     return items[item_id]
#
#
# @app.get('/items/{items_id}/public',
#          response_model=Item,
#          tags=['Items'],
#          response_model_exclude=['tax'])
# async def read_item_public_data(item_id: Literal['foo', 'bar', 'baz']):
#     return items[item_id]
#


# @app.post('/user/', response_model=UserOut)
# async def create_user(user: UserIn):
#     return user
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
# class UserInDB(UserBase):
#     hashed_password: str
#
# def fake_password_hashed(raw_password: str):
#     return f'supersecret{raw_password}'
#
#
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hashed(user_in.password)
#     print(hashed_password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print('user saved')
#     print('user_in.dict', user_in.dict())
#     return user_in_db
#
#
# @app.post('/user/',
#           tags=['User'],
#           description='User Create',
#           response_model=UserOut,
#           )
# async def create_user(user_in: UserIn):
#     print(user_in)
#     user_saved = fake_save_user(user_in)
#     return user_saved
#
#
# class ItemBase(BaseModel):
#     description: str
#     type: str
#
# class CarItem(ItemBase):
#     type = 'car'
#
#
# class PlaneItem(ItemBase):
#     type = 'plane'
#     size: int
#
#
# class ListItem(BaseModel):
#     name: str
#     description: str
#
#
# list_item = [
#     {'name': 'Foo', 'description': 'There comes my hero'},
#     {'name': 'Red', 'description': 'It\'s my aeroplane'},
#
# ]
#
# items = {
#     'item1': {'description': 'All my friends drive a low rider', 'type': 'car'},
#     'item2': {'description': 'Music is y aeroplane it\'s my aeroplane', 'type': 'plane', 'size': 5}
# }
#
# @app.get('/items/{item_id}',
#          tags=['Items'],
#          response_model= PlaneItem | CarItem)
# async def read_item(item_id: Literal['item1', 'item2']) -> PlaneItem | CarItem :
#     return items[item_id]
#
#
# @app.get('/list_items/',
#          tags=['Items'],
#          response_model=list[ListItem])
# async def read_image():
#     return items
#
# @app.get('/arbitrary/',
#          tags=['Items'],
#          response_model=dict[str, float])
# async def get_arbitrary():
#     return {'foo': 1, 'bar': '2'}

@app.post('/items/',
          tags=['Items'],
          status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {'name': name}


@app.delete('/items/{primary_key}',
          tags=['Items'],
          status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(primary_key: str):
    return {'primary_key': primary_key}
