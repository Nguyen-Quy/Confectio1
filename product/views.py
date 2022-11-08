from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        if product != None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            raise Http404()


class CategoryDetail(APIView):
    def get(self, request, category_slug, format=None):
        category = Category.objects.get(slug=category_slug)
        if category != None:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            raise Http404()


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
