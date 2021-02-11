from django.db import models
from accounts.models import Member

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, default="none")

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.URLField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='menus')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MoneyTransaction(models.Model):
    sender = models.OneToOneField(Member, on_delete=models.PROTECT, related_name="transfered_money_transaction")
    receiver = models.OneToOneField(Member, on_delete=models.PROTECT, related_name="received_money_trainsaction")
    amount = models.IntegerField()
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.amount}]{self.sender} => {self.receiver}"

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="orders")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")
    orderer = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="order")
    members = models.ManyToManyField(Member, related_name="orders")
    total_delivery_fee = models.IntegerField()
    state = models.CharField(max_length=20) # ordering state: receiving order, finished order
    total_money = models.IntegerField()
    transactions = models.ForeignKey(MoneyTransaction, on_delete=models.CASCADE, blank=True, null=True)
    is_finished = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.orderer}: {self.menu}"
