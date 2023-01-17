from django.contrib import admin
from User.models import Team, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


admin.site.register(Team)
admin.site.register(User, UserAdmin)
