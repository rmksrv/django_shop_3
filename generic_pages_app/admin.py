from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import GenericPage


@admin.register(GenericPage)
class GenericPageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "updated_at",
        "available",
    ]
    list_filter = ["available", "updated_at", "created_at"]
    list_editable = ["available"]
    prepopulated_fields = {"slug": ("title",)}
