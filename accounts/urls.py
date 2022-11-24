from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    ### --------------Accounts-------------###
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('staff/', views.staff, name='staff'),
    ### -------------Admin page------------###
    path('dashboard/', views.order_dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    # path('orders/', views.OrderList.as_view(), name='order_list'),
    # path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_status'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]
for url in urlpatterns:
    print(url)
