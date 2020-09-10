from django.urls import path, include
from .views import ChatAPI, room

urlpatterns = [
    path('api/', ChatAPI.as_view()),
    path('<str:room_name>/', room, name='room'),
]