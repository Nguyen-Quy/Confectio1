from django.db.models import Q
from django.http import Http404, HttpRequest

# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.core.paginator import EmptyPage, Paginator

PRODUCTS_PER_PAGE = 9

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    category_queryset = Category.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', ]
    lookup_field = 'slug'

    @action(detail=False, methods=['get'], url_path='lastest',)
    def lastest_product(self, request, format=None):
        lastest = self.get_queryset().order_by('-date_added')[0:6]
        # serializer = self.get_serializer_class()(latest)
        serializer = ProductSerializer(lastest, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='allproducts',)
    def all_product(self, request, format=None):
        page = request.GET.get('page',1)
        allproducts = self.get_queryset()
        product_paginator = Paginator(allproducts, PRODUCTS_PER_PAGE)
        try:
            allproducts = product_paginator.page(page)
            serializer = ProductSerializer(allproducts, many=True)
        except EmptyPage:
            allproducts = product_paginator.page(product_paginator.num_pages)
            serializer = ProductSerializer(allproducts, many=True)
        except:
            allproducts = product_paginator.page(PRODUCTS_PER_PAGE)
            serializer = ProductSerializer(allproducts, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    product_queryset = Product.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', ]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'], url_path='(?P<product_slug>[^/.]+)')
    def get_product_detail(self, request, slug, product_slug):
        product = Product.objects.get(category__slug=slug, slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@ api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
