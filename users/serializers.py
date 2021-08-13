from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, Profile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'agent_code', 'username', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Profile
        fields = (
            'id', 'user', 'username', 'full_name', 'profile_pic', 'get_profile_picture')

        read_only_fields = ['user']

    def get_username(self, profile):
        username = profile.user.username
        return username
