from datetime import datetime

from pydantic import BaseModel


class Book(BaseModel):
    id: str
    author: str
    title: str
    genre: str
    price: str
    publish_date: str
    description: str
