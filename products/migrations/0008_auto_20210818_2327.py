# Generated by Django 3.2.6 on 2021-08-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productmodel_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ProductTagModel',
        ),
    ]