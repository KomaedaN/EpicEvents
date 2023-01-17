from django.contrib import admin
from Client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'company_name')


admin.site.register(Client, ClientAdmin)
