from django.urls import path
from testapp1 import views

urlpatterns = [
    path('', views.index_view),
    path('addmovie/', views.addmovie_view),
    path('listmovie/', views.listmovie_view),
]