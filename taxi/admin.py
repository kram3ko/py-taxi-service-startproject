import random
import string

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "license_number",
                    "generate_license_button",
                )
            },
        ),
    )

    readonly_fields = ("generate_license_button",)

    def generate_license_button(self, obj: object = None) -> any:  # noqa: ARG002
        return format_html(
            '<button type="button" onclick="document.getElementById('
            "'id_license_number').value = '{}';\" class=\"button\">"
            "Generate License</button>",
            "".join(
                random.choices(string.ascii_uppercase + string.digits, k=12)
            ),
        )

    generate_license_button.short_description = "Generate Licence"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "manufacturer",
    ]
    search_fields = [
        "model",
    ]
    list_filter = [
        "manufacturer",
    ]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "country",
    ]
