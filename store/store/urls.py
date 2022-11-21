from django.contrib import admin
from django.urls import path

from cars.views import CarsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cars/', CarsView.App.urls),
]
