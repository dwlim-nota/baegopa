from django.shortcuts import render
from .models import Menu

# Create your views here.
def order(req):
    context = {}
    menus = Menu.objects.all()
    context["menus"] = menus
    return render(req, 'order/order.html', context=context)

def slack(req):
    # TODO: fill here
    return ""