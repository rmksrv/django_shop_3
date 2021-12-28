from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from image_cropping import ImageCropField, ImageRatioField

from .constants import CATEGORIES_IMAGE_LOCATION, PRODUCTS_IMAGE_LOCATION
from generic_pages_app.constants import NO_IMAGE_PATH


class Category(models.Model):
    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Имя", max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to=CATEGORIES_IMAGE_LOCATION,
        null=True,
        blank=False,
        default=NO_IMAGE_PATH,
    )
    cropping = ImageRatioField("image", "1000x1000", verbose_name="Обрезать изображение")

    def absolute_url(self):
        return reverse("category-product-list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductDescriptionParagraph(models.Model):
    class Meta:
        verbose_name = "Абзац"
        verbose_name_plural = "Описание товара"

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="Порядок появления")
    text = RichTextField(verbose_name="Текст", config_name="main", null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение", null=True, blank=True)
    cropping = ImageRatioField("image", "1000x1000", verbose_name="Обрезать изображение")

    def __str__(self):
        return str(self.order)


class Product(models.Model):
    class Meta:
        ordering = (
            "updated_at",
            "name",
        )
        index_together = (("id", "slug"),)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        related_name="products",
        on_delete=models.CASCADE,
    )
    name = models.CharField(verbose_name="Наименование", max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to=PRODUCTS_IMAGE_LOCATION,
        blank=False,
        default=NO_IMAGE_PATH,
    )
    cropping = ImageRatioField("image", "1000x1000", verbose_name="Обрезать изображение")
    preview_description = models.CharField(verbose_name="Краткое описание", max_length=255, blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField(verbose_name="Доступное для продажи количество")
    available = models.BooleanField(verbose_name="Товар доступен", default=True)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Последнее обновление", auto_now=True)

    # TODO: уверен, что это не Django-way
    @property
    def description_paragraphs(self):
        return ProductDescriptionParagraph.objects.filter(product_id=self.id).order_by("order")

    def absolute_url(self):
        return reverse("product-detail", args=[self.slug])

    def __str__(self):
        return self.name
