# Generated by Django 3.1.5 on 2021-02-15 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20210214_2257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
    ]
