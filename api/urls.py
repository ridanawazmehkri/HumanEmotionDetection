from django.urls import path

from . import views

urlpatterns = [path("api/getQ", views.process_image), ]