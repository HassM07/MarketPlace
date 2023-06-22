from django.contrib import admin
from .models import ExtendedUser, Item, LikedItems
# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Item)
admin.site.register(LikedItems)