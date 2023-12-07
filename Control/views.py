from django.shortcuts import render,redirect,get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . models import Empleado,Conductor

#mapa
from django.conf import settings
from .mixins import Directions


#metodos#
@login_required
# Create your views here.
def BASE(request):
    return render(request,'base.html')

def tablas(request):
    empleados = Empleado.objects.all() 
    return render(request,"tablas.html",{"empleados":empleados})

def Location(request):
    return render(request,"Location.html")

def registro(request):
    return render(request,'registration/registro.html')

def salida(request):
    logout(request)
    return redirect('/')

#class Inicio(LoginRequiredMixin, generic.TemplateView):
#    template_name = 'Templates/base.html'
#    login_url = 'Ctrl:login'

def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'route.html', context)	


'''
Basic view for displaying a map 
'''
def map(request):

	lat_a = request.GET.get("lat_a", None)
	long_a = request.GET.get("long_a", None)
	lat_b = request.GET.get("lat_b", None)
	long_b = request.GET.get("long_b", None)
	lat_c = request.GET.get("lat_c", None)
	long_c = request.GET.get("long_c", None)
	lat_d = request.GET.get("lat_d", None)
	long_d = request.GET.get("long_d", None)


	#only call API if all 4 addresses are added
	if lat_a and lat_b and lat_c and lat_d:
		directions = Directions(
			lat_a= lat_a,
			long_a=long_a,
			lat_b = lat_b,
			long_b=long_b,
			lat_c= lat_c,
			long_c=long_c,
			lat_d = lat_d,
			long_d=long_d
			)
	else:
		return redirect(reverse('Control:route'))

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"lat_c": lat_c,
	"long_c": long_c,
	"lat_d": lat_d,
	"long_d": long_d,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,

	}
	return render(request, 'map.html', context)
