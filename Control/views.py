from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
# Create your views here.
def BASE(request):
    return render(request,'base.html')


def registro(request):
    return render(request,'registration/registro.html')

def salida(request):
    logout(request)
    return redirect('/')

#class Inicio(LoginRequiredMixin, generic.TemplateView):
#    template_name = 'Templates/base.html'
#    login_url = 'Ctrl:login'