from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Category, Product, ProductDescriptionParagraph


class ProductDescriptionParagraphInline(ImageCroppingMixin, admin.StackedInline):
    model = ProductDescriptionParagraph
    extra = 1


@admin.register(Category)
class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [ProductDescriptionParagraphInline]
    list_display = [
        "name",
        "category",
        # "price",
        "available",
        "created_at",
        "updated_at",
    ]
    list_filter = ["available", "created_at", "updated_at", "category"]
    list_editable = ["available"]
    prepopulated_fields = {"slug": ("name",)}
