from django.urls import path

from .views import (AttendantRentListView, CarDetailView, CarListView,
                    RentListView, rent_car, rent_recive_car)

urlpatterns = [
    path("car/", CarListView.as_view(), name="list_cars"),
    path("car/<str:pk>/", CarDetailView.as_view(), name="detail_car"),
    path("car/rent/<str:car_plate>/", rent_car, name="rent_car"),
    path("rent/", RentListView.as_view(), name="list_rents"),
    path("rent/<str:rental_number>/recive",
         rent_recive_car, name="rent_recive_car"),
    path("rent/attendant/", AttendantRentListView.as_view(),
         name="attendant_list_rents"),
]
