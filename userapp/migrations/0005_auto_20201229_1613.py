# Generated by Django 3.1.4 on 2020-12-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20201229_1547'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
