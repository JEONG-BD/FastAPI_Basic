from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
    id : str 
    item : str 


class TodoItem(BaseModel):
    item : str 
    
    class Config : 
        schema_extra = {
            'example': {
                'item' : 'Read the next chater of the book'
            }
        }


class TodoItems(BaseModel):
    todos : List[TodoItem]
    
    class Config:
        schema_extra = {
            'example': {
                'todos':[
                    {
                        'item':'Example Schema 1!'
                    }, 
                    {
                        'item':'Example Schema 2!'
                    },
                    {
                        'item':'Example Schema 3!'
                    },
                ]
            }
        }
    