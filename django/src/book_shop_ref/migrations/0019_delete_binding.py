# Generated by Django 3.1.3 on 2020-11-08 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_remove_book_type_binding'),
        ('book_shop_ref', '0018_binding'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Binding',
        ),
    ]
