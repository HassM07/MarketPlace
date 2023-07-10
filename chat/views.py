from django.shortcuts import render
from django.http import HttpResponse
from .models import Chat
from extendedUser.models import ExtendedUser
# Create your views here.


def home_view(request):
    user = ExtendedUser.objects.get(user=request.user)
    # Chats are sorted by how long ago they were interacted with
    chats = user.chat_set.all().order_by('-latestInteraction')

    return render(request, 'chatHome.html', {'chats': chats})


def chat_view(request, chat_id):
    user = ExtendedUser.objects.get(user=request.user)
    chats = user.chat_set.all().order_by('-latestInteraction')
    chat = Chat.objects.get(id=chat_id)
    print(chat.id)
    return render(request, 'chatShow.html', {'chats': chats, 'mainChat': chat})
