from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CakeForm
from .models import Cake


# Create your views here.

def add_cake_page(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Cake added successfully!")
            return redirect('home_page')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CakeForm()
    return render(request, 'add_cake_page/add.html', {'form': form})


def home_page(request):
    cakes = Cake.objects.all()
    return render(request, 'home_page/index.html', {'cakes': cakes})
