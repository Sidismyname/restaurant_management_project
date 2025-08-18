from django.urls import path
from .views import about, home

urlpatterns = [
    path("",views.home, name="home_view"),
    path("about/",views.about,name="about_view")
]