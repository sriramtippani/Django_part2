from django.urls import path
from . import views

urlpatterns = [
    path('', views.f1),
    path('sports/', views.sports_view),
    path('movies/', views.movies_view),
    path('politics/', views.politics_view),
]