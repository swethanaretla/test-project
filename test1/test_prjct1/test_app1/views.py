from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def login(request):
	print ("swetha")
	return HttpResponse("swetha app")
