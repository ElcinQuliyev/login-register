from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'image')

admin.site.register(User, UserAdmin)