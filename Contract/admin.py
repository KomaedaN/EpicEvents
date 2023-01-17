from django.contrib import admin
from Contract.models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'client')


admin.site.register(Contract, ContractAdmin)
