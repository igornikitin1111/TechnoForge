from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserForge
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

class UserForgeAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "phone")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(UserForge, UserForgeAdmin)