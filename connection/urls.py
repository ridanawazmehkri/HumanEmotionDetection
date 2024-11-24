from django.urls import path
from connection import views

urlpatterns = [
    path("", views.home,name='home'),
    path("/demo",views.camera,name='dem'),
    path("/team",views.team,name="team"),
    path("/about",views.about,name="about"),
    
    
]