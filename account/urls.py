from django.urls import path
from .views import  RequestPasswordResetEmail

urlpatterns = [
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
]
