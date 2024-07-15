from django.contrib import admin
from . import models

admin.site.register(
    models.Category,
)


@admin.register(models.Product)
class Productadmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_editable = ("name",)
