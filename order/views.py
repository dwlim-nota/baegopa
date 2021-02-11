from django.shortcuts import render
from .models import Store

# Create your views here.
def order(req):
    context = {}
    stores = Store.objects.all()
    context["stores"] = stores
    return render(req, 'order/order.html', context=context)

def menu_details(req):
    return render(req, 'order/menu_details.html')

def slack(req):
    # TODO: fill here
    return ""