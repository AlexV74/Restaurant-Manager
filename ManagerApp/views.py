from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import MenuCategory, MenuItems, Order, Item, Table, Payment
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.db.models import Sum

def activeorders(request):
    """
    Shows orders that have been placed and have not been completed yet
    """
    orders = Order.objects.filter(preparing=True).values()
    items = Item.objects.filter(previous__isnull=True)
    count = Item.objects.all().count()
    context = {
        'orders': orders,
        'items': items,
        'count': count,
  }
    return render (
        request,
        'ManagerApp/activeorders.html',
        context
    )
    
def ReadyToDeliver(request, id):
    """
    Filters and shows which orders are finished cooking and are ready to be delivered
    """
    Order.objects.filter(order_id=id).update(preparing=False)
    return HttpResponseRedirect('/activeorders')


def home(request):
    """
    Shows the homepage, which is the customer facing part of the app.
    """
    request.session.setdefault("Table", 0)
    categories = MenuCategory.objects.all()
    menu_items = MenuItems.objects.all()
    basketItems = Item.objects.filter(order = 0).values()
    dict = basketItems.aggregate(Sum('price'))

    if dict['price__sum'] is None:
        totalPrice = None
    else:
        totalPrice = round(dict['price__sum'], 2) 
        
    return render(request, 'ManagerApp/home.html', {'categories': categories, 'menu_items': menu_items, 'basketItems': basketItems, 'totalPrice': totalPrice})

def menu_item_details(request, item_id):
    """
    Gives more details on the specific item.
    """
    item = get_object_or_404(MenuItems, item_id=item_id)
    return render(request, 'menu_item_details.html', {'item': item})

# Set the table number from user submitted value from post request
def tableNumber(request):
    """
    Sets the table number from user submitted value from post request
    """
    request.session["Table"] = request.POST.get('table')
    return HttpResponseRedirect("/home")


def call_waiter(request):
    req_help = Table(table_number = request.session["Table"])
    req_help.need_help = True
    req_help.save()
    return HttpResponseRedirect('/home')
    

def SubmitOrder(request):
    """
    Submit the order when the customer goes through checkout
    """
    currentOrder = Order(table_number = request.session["Table"]) 
    currentOrder.save()
    print(currentOrder.order_id)
    Item.objects.filter(order = 0).update(order = currentOrder.order_id)
   
    return HttpResponseRedirect("/home")


def addItem(request, iname, item_id):
    """
    Add the item to the basket
    """
    menuItem = MenuItems.objects.get(item_id = item_id)
    print(menuItem.price)
    quantity = int(request.POST.get(f"{item_id}_quantity"))
    for i in range(quantity):
        item = Item(iname=iname, order=0, price=menuItem.price)
        print(item.price)
        item.save()
    return HttpResponseRedirect("/home")


def waiter(request):
    """
    Render the waiter page, waiter can see orders and their status
    """
    preparingOrders = Order.objects.filter(preparing=True).values()
    readyOrders = Order.objects.filter(preparing=False).values()
    items = Item.objects.filter(previous__isnull=True)
    need_help = Table.objects.filter(need_help = True)
    context = {
        'preparingOrders': preparingOrders,
        'readyOrders': readyOrders,
        'items': items,
        'need_help': need_help,
  }
    return render (
        request,
        'ManagerApp/waiter.html',
        context
    )

def about(request):
    """
    Render the about us page
    """
    return render (
        request,
        'ManagerApp/about.html'
    )
def contactus(request):
    """
    Render the contact us page
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'New message from {name}'
        body = f'Name: {name}\nEmail: {email}\n\n{message}'
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['team5rest@outlook.com'])
    return render (
        request,
        'ManagerApp/contactus.html'
    )

def checkout(request):
    """
    Renders the checkout, showing the items in the basket
    """
    basketItems = Item.objects.filter(order = 0).values()
    dict = basketItems.aggregate(Sum('price'))
    totalPrice = round(dict['price__sum'], 2) 

    return render (
        request,
        'ManagerApp/checkout.html',
        {'basketItems': basketItems, 'totalPrice': totalPrice}
    )

def Delivered(request, id): # May need changing once customer checkout has been implemented.
    """
    Deletes an order from the order table since the order has been delivered
    """
    Order.objects.filter(order_id=id).delete()
    return HttpResponseRedirect('/waiter')

def Help_given(request, table_number):
    table = Table.objects.get(table_number=table_number)
    table.need_help = False 
    table.save()
    return HttpResponseRedirect('/waiter')


def CancelOrder(request, id):
    """
    Deletes an order since it's been cancelled by the customer
    """
    Order.objects.filter(order_id=id).delete()   
    return HttpResponseRedirect('/waiter')

@csrf_protect
def payment(request):
    if request.method == 'POST':
        cardholder_name = request.POST['cardholder_name']
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvv = request.POST['cvv']
        amount = request.POST['amount']

        # Create a new Payment object and save it to the database
        payment = Payment(cardholder_name=cardholder_name, card_number=card_number, expiry_date=expiry_date, cvv=cvv, amount=amount)
        payment.save()
    
    # Render the payment form
    return render(request, 'ManagerApp/checkout.html')

