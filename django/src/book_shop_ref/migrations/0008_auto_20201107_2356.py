# Generated by Django 3.1.2 on 2020-11-07 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop_ref', '0007_publishinghouse_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='Москва', max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='city',
            field=models.ForeignKey(default='Москва', on_delete=django.db.models.deletion.PROTECT, related_name='publishing_houses', to='book_shop_ref.city', verbose_name='Город'),
        ),
    ]
