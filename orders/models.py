from django.db import models
from django.contrib.auth.models import User

#團購主題
class GroupBuy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="groupbuys")
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    drink_mode = models.BooleanField(default=False)  # 飲料模式

    def __str__(self):
        return self.title


#品項
class Item(models.Model):
    groupbuy = models.ForeignKey(GroupBuy, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


#使用者訂購紀錄
class OrderRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groupbuy = models.ForeignKey(GroupBuy, on_delete=models.CASCADE, null=True)

    item_name = models.CharField(max_length=100)   # 使用者自己填
    note = models.TextField(blank=True, null=True) # 備註
    drink_name = models.CharField(max_length=100)

    order_time = models.DateTimeField(auto_now_add=True)

    sweetness = models.CharField(max_length=20, blank=True, null=True)
    ice = models.CharField(max_length=20, blank=True, null=True)