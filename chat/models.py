from django.db import models
from extendedUser.models import ExtendedUser, Item
# Create your models here.


class Chat(models.Model):
    users = models.ManyToManyField(ExtendedUser)
    createdAt = models.DateTimeField(auto_now_add=True)
    Item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)

