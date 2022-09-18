from django.urls import path
from . import views

urlpatterns = [
    path('dao/', views.DAO_list)
]