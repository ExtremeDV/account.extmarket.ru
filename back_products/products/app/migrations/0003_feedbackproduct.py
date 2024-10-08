# Generated by Django 5.0.7 on 2024-08-24 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_category_product_certificate_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(verbose_name='Оценка продукта')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Изображение 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Изображение 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Изображение 3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Изображение 4')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Изображение 5')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Отзыв о продукте',
                'verbose_name_plural': 'Отзывы о продуктах',
            },
        ),
    ]
