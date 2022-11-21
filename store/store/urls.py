from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

api = NinjaAPI()

from cars.views import CarsView
from users.views import UsersView

api.add_router('/cars/', CarsView.router)
api.add_router('/users/', UsersView.router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
