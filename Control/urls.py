from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from .views import Inicio
app_name = "Control"

urlpatterns = [
    path('', views.BASE, name="BASE" ),
    path('tablas/',views.tablas, name="tablas"),
    path('salida/',views.salida, name="salida"),
    path('registro/',views.registro, name="registro"),
    path('map/',views.map, name="map"),
    path('route/',views.route, name="route"),
    path('Location/',views.Location, name="Location"),
    #path('',Inicio.as_view(), name="inicio"),
    #urls de inicio de sesion
    #path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),

]
