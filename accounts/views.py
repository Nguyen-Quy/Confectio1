from django.db.models import Count
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import Http404
from rest_framework import permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .forms import SignUpForm, LoginForm, OrderForm

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer
from product.models import Product
from .models import User
from .filters import OrderFilter


"""Accounts registration"""


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return render(request, 'accounts/login.html', {'form': form, 'msg': msg})
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return render(request, 'accounts/admin.html')
            if user is not None and user.is_customer:
                login(request, user)
                return render(request, 'accounts/customer.html')
            if user is not None and user.is_staff:
                login(request, user)
                return render(request, 'accounts/staff.html')
            else:
                msg = 'invalid credential'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


def adminpage(request):
    return render(request, 'accounts/admin.html')


def customer(request):
    return render(request, 'accounts/customer.html')


def staff(request):
    return render(request, 'accounts/staff.html')


"""Admin page"""


def order_dashboard(request):
    orders = Order.objects.all().order_by('-status')[0:5]
    # print('order', orders.values())
    items = OrderItem.objects.filter(order__id__in=orders.all()).values(
        'order_id').values('product_id')
    products = Product.objects.filter(id__in=items)

    zipped_order = zip(orders, products)

    customers = User.objects.filter(is_customer=True)
    total_customer = customers.count()

    customer_order = Order.objects.filter(
        user__id__in=customers.all()).values('user_id').annotate(n=Count('user_id'))

    # for co in customer_order:
    #     print('customer: ', co['user_id'])
    #     print('order: ', co['user_id__count'])

    zipped_lst = zip(customers, customer_order)

    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'customer_order': customer_order,
        'total_customer': total_customer,
        'total_orders': total_orders,
        'list': zipped_lst,
        'olist': zipped_order,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'adminpage/dashboard.html', context)


def customer(request, pk):
    customer = User.objects.get(id=pk)
    phone = Order.objects.filter(user_id__in=pk)[0]
    orders = Order.objects.filter(user__id=customer.id)
    items = OrderItem.objects.filter(order__id__in=orders).values('product_id')
    products = Product.objects.filter(id__in=items)
    zipped_order = zip(orders, products)

    total_orders = orders.count()
    items = OrderItem.objects.filter(order_id__in=orders)
    # print(items)

    context = {
        'customer': customer,
        'orders': orders,
        'items': items,
        'phone': phone,
        'total_orders': total_orders,
        'olist': zipped_order,

        # 'list': zipped_lst
    }
    return render(request, 'adminpage/customer.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'adminpage/products.html', context)


def updateOrder(request, pk):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # return redirect('/customer/'+str(order.user_id))
            return redirect('/accounts/customer/'+str(order.user_id))
    context = {'action': action, 'form': form}
    return render(request, 'adminpage/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        customer_id = order.user_id
        customer_url = '/accounts/customer/'+str(customer_id)
        order.delete()
        return redirect(customer_url)
    return render(request, 'adminpage/delete_item.html', {'item': order})
