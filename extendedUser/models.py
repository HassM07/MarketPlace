from django.db import models
from django.contrib.auth.models import User  # Used as our base User Model


# Create your models here.

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()

    def get_user(self):
        return self.user


class Item(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=3, default=0, null=False)
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(null=True, default='')

    # ToDo Images

    def __str__(self):
        return self.title

    def get_user(self):
        return self.user

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description


class LikedItems(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.get_username()} Liked {self.item.title}"

    def get_user(self):
        return self.user

    def get_item(self):
        return self.item


class Basket(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.user.user.get_username()}'s Basket"

    def get_user(self):
        return self.user

    def get_items(self):
        return self.items
