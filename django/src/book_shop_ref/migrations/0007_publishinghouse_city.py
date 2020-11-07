# Generated by Django 3.1.2 on 2020-11-07 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop_ref', '0006_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishinghouse',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='publishing_houses', to='book_shop_ref.city', verbose_name='Город'),
        ),
    ]
