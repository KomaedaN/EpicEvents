from rest_framework.serializers import ModelSerializer
from Contract.models import Contract


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['id', 'date_created', 'date_updated', 'client', 'contract']
        extra_kwargs = {'sales_contact': {'required': False}}
