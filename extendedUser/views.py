from django.shortcuts import render, redirect
from .forms import ExtendedUserForm, ItemForm, NewUserCreationForm
from .models import ExtendedUser, Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home_view(request):
    return render(request, 'userHomePage.html', {})


def user_register(request):
    if request.method == 'POST':
        # Todo Add messages for errors and success
        form_extended = ExtendedUserForm(request.POST)
        form_user = NewUserCreationForm(request.POST)
        if form_extended.is_valid() and form_user.is_valid():
            form_user.save()  # Creates the user
            username = form_user.cleaned_data['username']
            user = User.objects.get(username=username)  # Gets the user so that the extended user can be made
            e_user = ExtendedUser.objects.create(user=user, test=form_extended.cleaned_data['test'])
            user = authenticate(request, username=form_user.cleaned_data['username'],
                                password=form_user.cleaned_data['password1'])  # User to be logged in
            login(request, user)
            return redirect('user_home')
    else:
        form_extended = ExtendedUserForm()
        form_user = NewUserCreationForm()
    return render(request, 'userForm.html',
                  {'extendedUser_form': form_extended, 'user_form': form_user})


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user_home')
    else:
        form = ItemForm()
    return render(request, 'itemForm.html', {'item_form': form})


def logout_user(request):
    logout(request)
    # Todo Add message
    return redirect('user_home')
