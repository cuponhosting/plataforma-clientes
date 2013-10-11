# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def home(request):
	return HttpResponse("Este redirecciona a servicios o a login si no ha iniciado sesion")

def login(request):
	return HttpResponse("Aqui va el formulario de login")	

@login_required()
def servicios(request):
	tal = "tallll333333ll"
	return render_to_response("servicios.html", {'tal':tal, 'user': request.user})	

@login_required()
def logout(request):
	return HttpResponse("Se hace el cierre de la sesion")		