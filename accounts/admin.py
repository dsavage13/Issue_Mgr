from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username", "email", "role", "team", "is_staff"
    ]
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (
            None, {
                    "classes": ("wide",),
                    "fields": ("email", "role", "team", "password_1", "password_2"),
                }
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "team")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)