# Generated by Django 3.1.2 on 2020-11-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20201108_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='', max_length=15, unique=True, verbose_name='ISBN'),
        ),
    ]
