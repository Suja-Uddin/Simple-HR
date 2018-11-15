from django.contrib import admin
from django.contrib import auth

from .models import User

admin.site.site_header = 'MISFIT Administration'        # Custom header in admin
admin.site.site_title = 'MISFIT Administration'
admin.site.unregister(auth.models.Group)                # Removing Groups from admin
admin.site.unregister(auth.models.User)                 # Removing auth users from admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('is_logged_in',)         # Prevent editing it from admin site


