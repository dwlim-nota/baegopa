from django.contrib import admin
from .models import Menu, Store, Order

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'store')

class StoreAdmin(admin.ModelAdmin):
    fields = ('name', )

class OrderAdmin(admin.ModelAdmin):
    display_list = (
        'menu',
        'store',
        'orderer',
        'members',
        'total_delivery_fee',
        'state',
        'total_money',
        'transactions',
        'is_finished',
        'created_at',
        'updated_at',
        )

admin.site.register(Menu, MenuAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)