from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hm),
    path('hyderabad/', views.hy),
    path('bangalore/', views.ba),
    path('pune/', views.pu),
]
