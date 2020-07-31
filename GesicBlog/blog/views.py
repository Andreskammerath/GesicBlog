from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
	return HttpResponse("Bienvenido a la lista de Blogs")