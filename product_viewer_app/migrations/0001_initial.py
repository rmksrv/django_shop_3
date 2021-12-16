# Generated by Django 4.0 on 2021-12-12 16:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(default=pathlib.PureWindowsPath('C:/Users/rmksr/PycharmProjects/impractical_python/django_shop_3/static/images/no_image.png'), null=True, upload_to='categories', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, default=pathlib.PureWindowsPath('C:/Users/rmksr/PycharmProjects/impractical_python/django_shop_3/static/images/no_image.png'), upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('preview_description', models.CharField(blank=True, max_length=255, verbose_name='Краткое описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='Доступное для продажи количество')),
                ('available', models.BooleanField(default=True, verbose_name='Товар доступен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_viewer_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('updated_at', 'name'),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductDescriptionParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Порядок появления')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_viewer_app.product')),
            ],
            options={
                'verbose_name': 'Абзац',
                'verbose_name_plural': 'Описание товара',
            },
        ),
    ]
