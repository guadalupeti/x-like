from django.contrib import admin
from .models import Post, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'profile_picture')
    search_fields = ('username', 'email')

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'profile_picture'
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'profile_picture'
            ),
        }),
    )
    
    
admin.site.register(Post)
admin.site.register(CustomUser)