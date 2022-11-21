from ninja import Router

from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


from .models import Cars
from .schema import CarSchema 


class CarsView():
    router = Router()

    @router.get("/")
    def view(request, car: str):
        car = get_object_or_404(Cars, id=car)
        return model_to_dict(car )

    @router.get("/")
    def view_all(request):
        cars = Cars.objects.all().order_by('price')
        carsSerialized =  [{'id': i.id, 'title': i.title, 'model': i.model, 'price': i.price, 'isPublic': i.isPublic} for i in cars]

        return {"result": carsSerialized}

    @router.get('/me')
    def view_me(request):
        return {'result': 'show a my cars'}

    @router.get("/me/listing")
    def View_all_me(request):
        return {'result': 'return all me'}

    @router.post("/")
    def create(request,  data: CarSchema):
        car = Cars(**data.dict())
        car.save()
        return {"result": data}

    @router.put("/")
    def update(request, car: str, data: CarSchema):
        car = get_object_or_404(Cars, id=car)
        for attr, value in data.dict().items():
            setattr(car, attr, value)

        car.save()
        return model_to_dict(car)

    @router.delete("/")
    def delete(request, car: str):
        car = get_object_or_404(Cars, id=car)
        car.delete()
        return {'result': 'deleted'}
