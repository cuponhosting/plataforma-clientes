# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from principal.models import *

#def home(request):
#	return HttpResponse("Este redirecciona a servicios o a login si no ha iniciado sesion")

def login(request):
	return render_to_response("login.html", {'tal':tal})	

@login_required(login_url='/login')
def servicios(request):
	tal = "tallll333333ll"
	
	#tal = request.user.username
	
	#tal =  dominios.objects.all().filter(dominio='juarbo.com')
	#tal =  dominios.objects.get(codigo='2342')
	#tal =  dominios.objects.get
	return render_to_response("servicios.html", {'tal':tal})	

@login_required(login_url='/login')
def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect('/servicios/')
	#return HttpResponse("Se hace el cierre de la sesion")		