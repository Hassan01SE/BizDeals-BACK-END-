from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser
from businessapp.models import Business, Category 

class CustomUserAdmin(UserAdmin):
    model = NewUser
    list_display = ('email', 'id' , 'user_name', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'id' , 'user_name', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'user_name', 'first_name', 'last_name',)
    ordering = ('email',)


admin.site.register(NewUser, CustomUserAdmin)


