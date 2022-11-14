from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from confectio.settings import CORS_ALLOWED_ORIGINS
from .utils import Util
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import UserForm, ProfileForm
# from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class RequestPasswordResetEmail(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            absurl = CORS_ALLOWED_ORIGINS[0] + '/reset-password/' + uid + '/' + token
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


# class ProfileUpdateView(APIView, LoginRequiredMixin):
#     user_form = UserForm
#     profile_form = ProfileForm

#     def post(self, request):

#         post_data = request.POST or None
#         file_data = request.FILES or None

#         user_form = UserForm(post_data, instance=request.user)
#         profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.error(request, 'Your profile is updated successfully!')
#             return HttpResponseRedirect(reverse_lazy('profile'))

#         context = self.get_context_data(
#                                         user_form=user_form,
#                                         profile_form=profile_form
#                                     )

#         return Response(context, status=status.HTTP_200_OK)