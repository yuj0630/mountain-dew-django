from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'list.html')

def map_view(request):
    return render(request, 'map_view.html')

def accounts(request):
    return render(request, 'login.html')