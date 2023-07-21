# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import CustomUserCreationForm

from .models import Account


class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm

    list_display = (
        "id",
        "email",
        "username",
        "phone",
        "first_name",
        "last_name",
        "middle_name",
        "role",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )

    list_editable = ('role',)  # Make the 'role' field editable in the list view
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )

    readonly_fields = ("date_joined", "last_login")

    def save_model(self, request, obj, form, change):
        if obj.role == "dispatcher":
            obj.is_staff = True
        obj.save()


admin.site.register(Account, AccountAdmin)
