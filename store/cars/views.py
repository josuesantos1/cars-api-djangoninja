from ninja import NinjaAPI

class CarsView():
    App = NinjaAPI()

    @App.get("/")
    def view(request, car: int):
        return {'result': 'car'}

    @App.get("/")
    def viewAll(request):
        return {"result": 'cars'}

    @App.get('/me')
    def viewMe(request, car: int):
        return {'result': 'show a my cars'}

    @App.get("/me/listing")
    def ViewAllMe(request):
        return {'result': 'return all me'}

    @App.post("/")
    def create(request):
        return {"result": 'created'}

    @App.patch("/")
    def update(request, car: int):
        return {"result": 'updated'}

    @App.delete("/")
    def delete(request, car: int):
        return {'result': 'deleted'}
