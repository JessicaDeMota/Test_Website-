from django.http import HttpResponse
from django.shortcuts import render


# view using render()
def index(request):
    return render(request, 'index.html')

def user(request):
    return render(request, 'index2.html')


