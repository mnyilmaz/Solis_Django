from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"), # passing an id into url, with that user can observe a specific information as: ../room/1/
]