from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the default User model
admin.site.unregister(User)

# Optionally, customize the UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

# Re-register the User model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)