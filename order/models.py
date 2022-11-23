# from django.contrib.auth.models import User
from accounts.models import User
from django.db import models
from django.conf import settings

from product.models import Product


class Order(models.Model):
    # user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=100, null=True, choices=STATUS, default='Pending')
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.user.username

    @property
    def items(self):
        item_info = self.orderitem_set.all()
        return str(item_info)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
