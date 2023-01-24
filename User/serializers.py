from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.response import Response
from User.models import User


class SignupSerializer(serializers.ModelSerializer):
    group = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'team', 'group']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

