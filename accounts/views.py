from django.db.models import Count
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import Http404
from rest_framework import permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .forms import SignUpForm, LoginForm

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
    customers = User.objects.filter(is_customer=True)
    total_customer = customers.count()

    customer_order = Order.objects.filter(user__id__in=customers.all())
    print('customer order: ', customer_order)

    order_items = OrderItem.objects.filter(order_id__in=customer_order)
    zipped_order = zip(customers, order_items)

    c = Product.objects.filter(id__in=order_items.values('product_id'))
    num = order_items.values('product_id').annotate(n=Count('product_id'))
    zipped_lst = zip(c, num)

    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'customer_order': customer_order,
        'order_list': zipped_order,
        'total_customer': total_customer,
        'total_orders': total_orders,
        # 'list': zipped_lst,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'adminpage/dashboard.html', context)


def customer(request, pk):
    customer = User.objects.get(id=pk)
    customer_order = Order.objects.filter(user_id=customer)
    print(customer_order)

    items = OrderItem.objects.filter(order_id__in=customer_order)
    print(items)

    c = Product.objects.filter(id__in=items.values('product_id'))
    num = items.values('product_id').annotate(n=Count('product_id'))
    zipped_lst = zip(c, num)
    print(zipped_lst)

    context = {
        'customer': customer,
        'customer_order': customer_order,
        'items': items,
        'list': zipped_lst,
    }
    return render(request, 'adminpage/customer.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'adminpage/products.html', context)


class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    permission_classes = [AllowAny, ]

    def get_object(self, pk, format=None):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def put(self, request, pk):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        orders = self.get_object(pk)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
