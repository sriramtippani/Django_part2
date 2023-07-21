from django.urls import path
from app_1 import views

urlpatterns = [
    path('home/', views.homepage_view),
    path('image/', views.imagepage_view),
    path('jform/', views.insertJava_view),
    path('update/<int:id>', views.updatejava_view),
    path('del/<int:id>', views.delete_view),
    path('pform/', views.insertpython_view),
    path('pupdate/<int:id>', views.updatepython_view),
    path('pdelete/<int:id>', views.deletepython_view),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
]

