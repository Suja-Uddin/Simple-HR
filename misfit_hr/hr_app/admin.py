from django.contrib import admin

# Register your models here.
from .models import User, Request

admin.site.register(User)