# Generated by Django 3.1.2 on 2020-11-07 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop_ref', '0010_binding'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Isbn',
        ),
    ]