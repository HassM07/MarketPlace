from django.db import models
from django.contrib.auth.models import User  # Used as our base User Model


# Create your models here.

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)


class Item(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=3, default=0, null=False)
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(null=True, default='')
    # ToDo Images


class LikedItems(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Basket(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)