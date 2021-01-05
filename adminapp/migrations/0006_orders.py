# Generated by Django 3.1 on 2021-01-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]