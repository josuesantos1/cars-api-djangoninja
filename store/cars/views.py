from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .models import Cars
from .schema import CarSchema
class CarsView():
    App = NinjaAPI()

    @App.get("/{car}")
    def view(request, car: str):
        car = get_object_or_404(Cars, id=car)
        return model_to_dict(car )

    @App.get("/")
    def view_all(request):
        cars = Cars.objects.all().order_by('price')
        carsSerialized =  [{'id': i.id, 'title': i.title, 'model': i.model, 'price': i.price, 'isPublic': i.isPublic} for i in cars]

        return {"result": carsSerialized}

    @App.get('/me')
    def view_me(request):
        return {'result': 'show a my cars'}

    @App.get("/me/listing")
    def View_all_me(request):
        return {'result': 'return all me'}

    @App.post("/")
    def create(request,  data: CarSchema):
        car = Cars(**data.dict())
        car.save()
        return {"result": data}

    @App.put("/")
    def update(request, car: str, data: CarSchema):
        car = get_object_or_404(Cars, id=car)
        for attr, value in data.dict().items():
            setattr(car, attr, value)

        car.save()
        return model_to_dict(car)

    @App.delete("/")
    def delete(request, car: str):
        car = get_object_or_404(Cars, id=car)
        car.delete()
        return {'result': 'deleted'}
