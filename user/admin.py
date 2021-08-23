from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('username', 'longitude', 'latitude', 'is_dudi', 'is_guru', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    search_fields = ()
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)