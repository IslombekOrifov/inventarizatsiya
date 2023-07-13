# Generated by Django 4.0.6 on 2023-07-10 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import index.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0017_remove_user_description_remove_user_is_responsible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, upload_to='static/images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='static/images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at_at', models.DateTimeField(auto_now=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='RoomsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.CharField(max_length=10, verbose_name='rooms')),
                ('floor', models.CharField(max_length=10, verbose_name='floor')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('schet', models.CharField(blank=True, max_length=255, null=True, verbose_name='schet')),
                ('room_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='room_number')),
                ('inventar_number', models.CharField(blank=True, max_length=255, unique=True, verbose_name='inventar_number')),
                ('seria_number', models.CharField(blank=True, max_length=70, null=True, verbose_name='seria_number')),
                ('images', models.ImageField(blank=True, upload_to=index.services.upload_image_path, verbose_name='images')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='status')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('year_of_manufacture', models.CharField(blank=True, max_length=50, null=True, verbose_name='year_of_manufacture')),
                ('unit_of_measurement', models.CharField(blank=True, max_length=50, null=True, verbose_name='unit_of_measurement')),
                ('product_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='count')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='index.category', verbose_name='category_id')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('model_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.model', verbose_name='model_id')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='responsible')),
            ],
        ),
    ]
