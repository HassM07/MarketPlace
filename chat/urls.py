from django.urls import path
from .views import home_view, chat_view

urlpatterns = [
    path('', home_view, name='chat_home'),
    path('<int:chat_id>', chat_view, name='chat_view'),
]
