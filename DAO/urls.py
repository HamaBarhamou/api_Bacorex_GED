from django.urls import path
from . import views

urlpatterns = [
    #path('dao/', views.DAO_list)
    path('dao/', views.DaoList.as_view()),
    path('dao/<int:pk>', views.DaoDetail.as_view())
]