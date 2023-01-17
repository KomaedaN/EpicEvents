from rest_framework.serializers import ModelSerializer
from Client.models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact']
