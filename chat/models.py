from django.db import models
from django.utils import timezone
from extendedUser.models import ExtendedUser, Item
from django.urls import reverse
# Create your models here.


class Chat(models.Model):
    users = models.ManyToManyField(ExtendedUser)
    createdAt = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128, null=False)
    latestInteraction = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.get_title()

    def get_users(self):
        return self.users

    def get_date(self):
        return self.createdAt

    def get_item(self):
        return self.item

    def get_title(self):
        return self.title

    def get_absolute_url(self):
        return reverse("chat_view", kwargs={'chat_id': self.id})


class Message(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False, default='')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def get_users(self):
        return self.user

    def get_date(self):
        return self.createdAt

    def get_content(self):
        return self.content

    def get_chat(self):
        return self.chat
