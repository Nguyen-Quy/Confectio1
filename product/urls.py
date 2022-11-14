from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, search
app_name = 'product'

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    # path('latest-products/', views.LatestProductsList.as_view()),
    # path('products/', views.AllProductsList.as_view()),
    # path('products/<slug:category_slug>/<slug:product_slug>/',ProductViewSet.get_detail()),

    path('products/search/', search),
    # path('categories/', views.Categories.as_view()),
    # path('products/<slug:category_slug>/', views.CategoryDetailSlug.as_view()),
]+router.urls

# for url in router.urls:
#     print(url, '\n')
