# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	return HttpResponse("Este redirecciona a servicios o a login si no ha iniciado sesion")

def login(request):
	return HttpResponse("Aqui va el formulario de login")	

def servicios(request):
	tal = "tallll333333ll"
	return render_to_response("servicios.html", {'tal':tal})	

def logout(request):
	return HttpResponse("Se hace el cierre de la sesion")		