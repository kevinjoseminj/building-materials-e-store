# Generated by Django 3.1 on 2021-01-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_remove_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
