from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import ExtendedUserForm, ItemForm
# Create your views here.


def home_view(request):
    return render(request, 'userHomePage.html', {})


def user_register(request):
    if request.method == 'POST':
        form = ExtendedUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user_home')
    else:
        form = ExtendedUserForm()
    return render(request, 'userForm.html', {'extendedUser_form': form})


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user_home')
    else:
        form = ItemForm()
    return render(request, 'itemForm.html', {'item_form': form})
