# Generated by Django 3.1.3 on 2020-11-08 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_book_type_binding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='type_binding',
        ),
    ]
