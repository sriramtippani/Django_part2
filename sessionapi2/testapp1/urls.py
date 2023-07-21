from django.urls import path
from . import views

urlpatterns = [
    path('add', views.additem_view),
    path('display/', views.display_view),
]