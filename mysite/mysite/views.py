from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin,Profile


# view using render()
def index(request):
    return render(request, 'index.html')

def user(request):
    return render(request, 'index2.html')

def listing(request):
    data = {
        "Admin": Admin.objects.all(),
        "Profiles":Profile.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "user.html",data)
