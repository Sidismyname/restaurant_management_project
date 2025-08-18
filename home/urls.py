from django.urls import path
from .views import *

urlpatterns = [
    path("",views.home, name"Home")
    path("about/",views.about,name="About Us")
]