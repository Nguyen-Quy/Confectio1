# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     contact_number = models.IntegerField()
#     profile_avt = models.ImageField(upload_to= "profiles/%Y/%m/%d", null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_added',)

#     def __str__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)