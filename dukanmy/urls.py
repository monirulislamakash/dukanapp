from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login,name="login"),
    path("",views.index,name="home"),
    path("otp/",views.otp,name="otp")
]
