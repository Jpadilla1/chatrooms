from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name',
                       'last_name', 'password1', 'password2')}),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
