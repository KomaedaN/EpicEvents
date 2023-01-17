from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from User.models import User, Team


class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'team']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

