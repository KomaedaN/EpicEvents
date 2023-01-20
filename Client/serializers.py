from rest_framework.serializers import ModelSerializer
from Client.models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ['id']
        extra_kwargs = {'sales_contact': {'required': False}}
