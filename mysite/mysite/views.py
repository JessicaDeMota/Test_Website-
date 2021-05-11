from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin,Profile
from django.contrib.auth.models import User
from .forms import UserForm, ContactForm
from .models import Contact

def index(request):

    return render(request, 'base.html')

def listing(request):
    data = {
        "Admin": Admin.objects.all(),
        "Profiles":Profile.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "user.html",data)

# view using render()
def administrator(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'admin.html',context={'users':users, 'form': form})



def contact(request):
    c = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})