from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    fields = ('name', 'price')

admin.site.register(Menu, MenuAdmin)