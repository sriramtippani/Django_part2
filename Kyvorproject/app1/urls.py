from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.homepage_view),
    path('list/', views.listpage_view, name='listpage'),
    path('insert/', views.insert_table_view),
    path('detail/<int:id>', views.detail_view),
    path('update/<int:id>', views.update_table_view),
    path('delete/<int:pk>', views.delete_table_view.as_view()),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
]
