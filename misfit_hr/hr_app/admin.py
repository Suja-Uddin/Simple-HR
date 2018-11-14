from django.contrib import admin

# Register your models here.
from .models import User, Request

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('is_logged_in',)