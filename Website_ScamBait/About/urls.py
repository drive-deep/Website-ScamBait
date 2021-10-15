from django.urls import path
from .views import About
urlpatterns = [
    path('', About,name="About"),
]