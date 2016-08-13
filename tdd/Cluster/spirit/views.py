from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def any(request):
	name = request.path.split('/')
	l=len(name) 
	return render(request,name[l-2]+'/'+name[l-1])

def home_page(request):
	return render(request,'home.html')

def start_page(request):
	return render(request,'elizabeth/start.html')

def throughleaves(request):
	return render(request,'elizabeth/throughleaves.html')
