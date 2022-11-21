from django.forms.models import model_to_dict
from ninja import Router

from .schema import UserSchema
from .models import User

class UsersView():
    router = Router()
    
    @router.post("/")
    def create(request, data: UserSchema):
        user = User(**data.dict())
        user.save()
        return model_to_dict(user)

    @router.get('/me')
    def view(request):
        return {'result': 'hi'}
