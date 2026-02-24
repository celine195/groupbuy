from django.contrib import admin
from .models import GroupBuy, Item, OrderRecord

admin.site.register(GroupBuy)
admin.site.register(Item)
admin.site.register(OrderRecord)