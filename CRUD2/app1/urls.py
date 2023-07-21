from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.homepage_view),
    path('durga/', views.users_view),
    path('list/', views.BeerList.as_view(), name='differentname'),
    path('detail/<int:pk>', views.BeerDetail.as_view(), name='anyname'),
    path('create/', views.BeerCreate.as_view()),
    path('update/<int:pk>', views.BeerUpdate.as_view()),
    path('delete/<int:pk>', views.BeerDelete.as_view()),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
]