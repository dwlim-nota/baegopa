from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('order/', views.order, name="order"),
    path('order/<str:menu_id>/', views.menu_details, name="menu_details"),
    path('slack/', views.slack, name="slack"),
]
