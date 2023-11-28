from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from .views import Inicio

urlpatterns = [
    path('', views.BASE, name="BASE" ),
    path('salida/',views.salida, name="salida"),
    path('registro/',views.registro, name="registro"),
    #path('',Inicio.as_view(), name="inicio"),
    #urls de inicio de sesion
    #path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),

]
