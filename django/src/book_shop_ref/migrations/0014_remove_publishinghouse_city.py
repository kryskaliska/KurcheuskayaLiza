# Generated by Django 3.1.2 on 2020-11-08 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop_ref', '0013_auto_20201108_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishinghouse',
            name='city',
        ),
    ]
