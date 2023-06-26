from django.urls import path
from .views import home_view, user_register

urlpatterns = [
    path('', home_view, name='user_home'),
    path('create', user_register, name='user_register'),
]
