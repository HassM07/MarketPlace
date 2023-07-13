from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chat, Message
from extendedUser.models import ExtendedUser
from .forms import MessageForm
from django.contrib import messages
# Create your views here.


def home_view(request):
    if not request.user.is_authenticated:
        messages.success(request, 'Please Login to use the Chat')
        return redirect('user_home')
    user = ExtendedUser.objects.get(user=request.user)
    # Chats are sorted by how long ago they were interacted with
    chats = user.chat_set.all().order_by('-latestInteraction')

    return render(request, 'chatHome.html', {'chats': chats})


def chat_view(request, chat_id):
    if not request.user.is_authenticated:
        messages.success(request, 'Please Login to use the Chat')
        return redirect('user_home')
    user = ExtendedUser.objects.get(user=request.user)
    chats = user.chat_set.all().order_by('-latestInteraction')
    chat = Chat.objects.get(id=chat_id)
    if request.method == 'POST':
        message_from = MessageForm(request.POST)
        if message_from.is_valid():
            Message.objects.create(user=user, content=message_from.cleaned_data['content'], chat=chat)
            return redirect(chat.get_absolute_url())
    else:
        message_from = MessageForm()

    chat_messages = chat.message_set.all().order_by('-createdAt')
    return render(request, 'chatShow.html',
                  {'chats': chats, 'mainChat': chat, 'messages': chat_messages,
                   'user': user, 'message_form': message_from})
