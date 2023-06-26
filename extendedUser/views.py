from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ExtendedUserForm
# Create your views here.


def home_view(request):
    return render(request, 'userHomePage.html', {})


def user_register(request):
    if request.method == 'POST':
        form = ExtendedUserForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('chat/')
    else:
        form = ExtendedUserForm()
    return render(request, 'userForm.html', {'form': form})
