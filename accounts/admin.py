from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    fields = ('user_id', 'name', 'bank_name', 'bank_account_number', 'password')

admin.site.register(Member, MemberAdmin)