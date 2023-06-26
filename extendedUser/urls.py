from django.urls import path
from .views import home_view, user_register, create_item

urlpatterns = [
    path('', home_view, name='user_home'),
    path('create', user_register, name='user_register'),
    path('createItem', create_item, name='create_item'),
]
