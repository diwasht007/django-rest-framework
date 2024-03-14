# Generated by Django 5.0.3 on 2024-03-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/products')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
