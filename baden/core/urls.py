from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('api/v1/apartments/', views.ApartmentApiView.as_view({'get': 'list'})),
    path('api/v1/apartment/<int:pk>/', views.ApartmentApiView.as_view({'get': 'retrieve'})),
]
