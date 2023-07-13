from django.shortcuts import render, redirect
from .forms import ExtendedUserForm, ItemForm, NewUserCreationForm, forms
from .models import ExtendedUser, Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


def home_view(request):
    return render(request, 'userHomePage.html', {'messages': messages.get_messages(request)})


def user_register(request):
    if request.method == 'POST':
        form_extended = ExtendedUserForm(request.POST)
        form_user = NewUserCreationForm(request.POST)
        if form_extended.is_valid() and form_user.is_valid():
            form_user.save()  # Creates the user
            username = form_user.cleaned_data['username']
            user = User.objects.get(username=username)  # Gets the user so that the extended user can be made
            e_user = ExtendedUser.objects.create(user=user, test=form_extended.cleaned_data['test'])
            login(request, user)  # Login user
            messages.success(request, 'Account created and Logged in')
            return redirect('user_home')
    else:
        form_extended = ExtendedUserForm()
        form_user = NewUserCreationForm()
    return render(request, 'userForm.html',
                  {'extendedUser_form': form_extended, 'user_form': form_user})


def create_item(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to create an item')
        return redirect('user_home')

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            user = ExtendedUser.objects.get(user=request.user)
            price = form.cleaned_data['price']
            title = form.cleaned_data['title']
            description = form.cleaned_data['title']
            Item.objects.create(user=user, price=price, title=title, description=description)

            messages.success(request, 'Item created')
            return redirect('user_home')
    else:
        form = ItemForm()
    return render(request, 'itemForm.html', {'item_form': form})


def user_logout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged')
        return redirect('user_home')

    logout(request)
    messages.success(request, 'Logged out')
    return redirect('user_home')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged In')
            return redirect('user_home')
    else:
        form = form = AuthenticationForm()
    return render(request, 'loginPage.html', {'login_form': form})
