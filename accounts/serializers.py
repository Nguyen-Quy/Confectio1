from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password',)

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'email already exists'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': 'username already exists'})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
