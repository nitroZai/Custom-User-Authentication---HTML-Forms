


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginn, name='loginn')
    ,path('loggedin/', views.loggedin, name="loggedin"),
    path('goingback/', views.goingback, name='goingback')
]