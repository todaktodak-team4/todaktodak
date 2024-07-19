from django.contrib import admin

# Register your models here.

from .models import rememberTree,Photo

# Register your models here.
admin.site.register(rememberTree)
admin.site.register(Photo)