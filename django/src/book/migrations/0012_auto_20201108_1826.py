# Generated by Django 3.1.3 on 2020-11-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20201108_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='age',
        ),
        migrations.RemoveField(
            model_name='book',
            name='type_binding',
        ),
    ]
