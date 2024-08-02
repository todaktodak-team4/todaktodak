from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname', 'date_joined', 'phone', 'address')
    readonly_fields = ('date_joined',)
    search_fields = ('username', 'email', 'nickname')
    fields = ('username', 'email', 'nickname', 'profile', 'phone', 'address', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)
