from django.urls import path
from .views import home_view, user_register, create_item, user_logout, user_login

urlpatterns = [
    path('', home_view, name='user_home'),
    path('signup', user_register, name='user_register'),
    path('createitem', create_item, name='create_item'),
    path('logout', user_logout, name='user_logout'),
    path('login', user_login, name='user_login'),
]
