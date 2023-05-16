from django.urls import path

from .views import CarDetailView, CarListView, RentListView, rent_car

urlpatterns = [
    path("car/", CarListView.as_view(), name="list_cars"),
    path("car/<str:pk>/", CarDetailView.as_view(), name="detail_car"),
    path("car/rent/<str:car_id>/", rent_car, name="rent_car"),
    path("rent/", RentListView.as_view(), name="list_rents"),
]
