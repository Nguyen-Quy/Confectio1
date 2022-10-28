from rest_framework import serializers
from .models import OrderItem, Order
from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )


class MyOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'strip_token',
            'items',
        )

    def get_items(self, obj):
        items_query = OrderItem.objects.filter(id=obj.id)
        serializers = OrderItemSerializer(items_query, many=True)

        return serializers.data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return Order


class MyOrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'strip_token',
            'items',
        )

    def get_items(self, obj):
        items_query = OrderItem.objects.filter(id=obj.id)
        serializers = OrderItemSerializer(items_query, many=True)
        return serializers.data
