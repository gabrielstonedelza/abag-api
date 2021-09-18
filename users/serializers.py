from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, AuthenticatedPhoneAddress


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'email', 'agent_code', 'username', 'phone', 'company_name', 'full_name', 'region', 'regional_code')


class AuthenticatedPhoneAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedPhoneAddress
        fields = ['agent', 'phone_mac_address', 'date_added']
