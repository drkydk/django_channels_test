from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
]