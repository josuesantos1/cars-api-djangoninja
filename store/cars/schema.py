from ninja import Schema
from .models import Cars

class CarSchema(Schema):
    title: str
    model: str
    price: float
    isPublic: bool

