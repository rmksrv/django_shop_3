from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse

from .constants import GENERIC_PAGES_IMAGE_LOCATION


class GenericPage(models.Model):
    class Meta:
        index_together = (("id", "slug"),)
        verbose_name = "Инфостраница"
        verbose_name_plural = "Инфостраницы"

    title = models.CharField(verbose_name="Название", max_length=80)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    text = RichTextField(verbose_name="Текст", config_name="main", null=True, blank=False)
    main_image = models.ImageField(verbose_name="Изображение", upload_to=GENERIC_PAGES_IMAGE_LOCATION)
    available = models.BooleanField(verbose_name="Доступна", default=True)
    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Последнее обновление", auto_now=True)

    def absolute_url(self):
        return reverse("page-detail", args=[self.slug])
