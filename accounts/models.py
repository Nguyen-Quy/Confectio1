from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_staff = models.BooleanField('Is staff', default=False)

    # @property
    # def orders(self):
    #     order_count = self.order_set.all().count()
    #     return str(order_count)
