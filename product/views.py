from django.db.models import Q

# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 9


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    http_method_names = ['get', ]
    lookup_field = 'slug'

    @action(detail=False, methods=['get'], url_path='latest',)
    def latest_product(self, request, format=None):
        latest = self.get_queryset().order_by('-date_added')
        # serializer = self.get_serializer_class()(latest)
        serializer = ProductSerializer(latest, many=True)
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
