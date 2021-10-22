# Generated by Django 3.2.5 on 2021-07-22 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_productmodel_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='wishlist',
            field=models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL, verbose_name='wishlist'),
        ),
    ]
