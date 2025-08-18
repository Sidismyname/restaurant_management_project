from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home_view"),
    path("about/",views.about,name="about_view")
]