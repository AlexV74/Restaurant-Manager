from django.urls import path, include
from ManagerApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("activeorders/", views.activeorders, name="activeorders"),
    path('activeorders/readytodeliver/<int:id>', views.ReadyToDeliver, name='ReadyToDeliver'),
    path("waiter/", views.waiter, name="waiter"),
    path('contactus/', views.contactus, name='contactus'),
    path("about/", views.about, name="about"),
    path("home/SubmitOrder/", views.SubmitOrder, name="SubmitOrder"),
    path("home/TableNumber/", views.tableNumber, name="tableNumber"),
    path('home/call_waiter/', views.call_waiter, name='call_waiter'),
    path("home/addItem/<str:iname>/<int:item_id>/", views.addItem, name="addItem"), 
    path("checkout/", views.checkout, name="checkout"),
    path('menuitem/<int:item_id>/', views.menu_item_details, name='menu_item_details'),
    path("waiter/CancelOrder/<int:id>", views.CancelOrder, name="CancelOrder"),
    path("waiter/HelpGiven/<int:table_number>", views.Help_given, name="HelpGiven"),
    path("waiter/Delivered/<int:id>", views.Delivered, name="Delivered"),
    path('payment/', views.payment, name='payment')
]
