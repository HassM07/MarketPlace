from django.db import models
from extendedUser.models import ExtendedUser, Item
# Create your models here.


class Chat(models.Model):
    users = models.ManyToManyField(ExtendedUser)
    createdAt = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)

    def get_users(self):
        return self.users

    def get_date(self):
        return self.createdAt

    def get_item(self):
        return self.item


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
