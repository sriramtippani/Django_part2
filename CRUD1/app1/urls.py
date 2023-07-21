from django.urls import path
from app1 import views

urlpatterns = [
    path('list/', views.BookView.as_view(), name='bookdelete'),
    path('<int:pk>/', views.BookDetail.as_view(), name='detail'),
    path('create/', views.BookCreate.as_view()),
    path('update/<int:pk>', views.BookUpdate.as_view()),
    path('delete/<int:pk>', views.BookDelete.as_view()),
]