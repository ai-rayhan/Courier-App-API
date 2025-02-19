from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['username', 'email', 'is_active','is_superuser','is_admin']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ( 'is_active','is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active','is_superuser','is_admin')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

    filter_horizontal = ()
    list_filter = ()

admin.site.register(User, CustomUserAdmin)

# myapp/admin.py

from django import forms
from django.contrib import admin
from .models import Role
class ChosenSelectMultiple(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs['data-placeholder'] = 'Select permissions'
        kwargs['attrs'] = attrs
        super().__init__(*args, **kwargs)

class RoleAdminForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'
        widgets = {
            'permissions': ChosenSelectMultiple(attrs={'style': 'width: 300px;'}),
        }

class RoleAdmin(admin.ModelAdmin):
    form = RoleAdminForm
    filter_horizontal = ('permissions',)

admin.site.register(Role, RoleAdmin)
