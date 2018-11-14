from django.contrib import admin
from django.contrib import auth

from .models import User

admin.site.site_header = 'MISFIT Administration'
admin.site.site_title = 'MISFIT Administration'
admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('is_logged_in',)


