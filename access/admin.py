from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from access.models import User
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    search_fields = ["email", "name"]
    readonly_fields = ["id", "uuid", "created_at", "updated_at"]

    list_display = [
        "email",
        "name",
        "is_admin",
        "created_at",
    ]

    list_filter = [
        "is_active",
        "is_admin",
        "created_at",
    ]

    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    add_fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "name",
                    "email",
                    "bio",
                ]
            },
        ),
        (
            _("Access"),
            {"fields": ["is_active", "is_admin"]},
        ),
    )

    filter_horizontal = []

    fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "id",
                    "uuid",
                    "name",
                    "email",
                    "password",
                    "bio",
                ]
            },
        ),
        (
            _("Access"),
            {
                "fields": [
                    "is_active",
                    "is_admin",
                ]
            },
        ),
        (_("Dates"), {"fields": ["created_at", "updated_at"]}),
    )

    class Media:
        pass
