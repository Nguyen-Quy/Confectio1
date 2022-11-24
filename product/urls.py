from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, search
app_name = 'product'

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('products/search/', search),
]+router.urls

