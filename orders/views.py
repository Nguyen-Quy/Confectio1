import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import OrderItem, Order
from .serializers import OrderSerializer, MyOrderSerializer

from cart.cart import Cart
from .forms import OrderCreateForm
from core import models, views
from product import models, views

# thư viện cho việc sử dụng email
# from confectio.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives


@api_view(['POST'])
@authentication_classes(authentication.TokenAuthentication)
@permission_classes(permissions.IsAuthenticated)
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get(
            'quantity')*item.get('product').price for item in serializer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount*100),
                currency='VND',
                description='Thanh toán từ Confectio',
                source=serializer.validated_data['stripe_token']
            )
            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
