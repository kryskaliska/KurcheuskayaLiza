# Generated by Django 3.1.2 on 2020-11-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Фамилия И.О.'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='book_shop.Author', verbose_name='Автор(ы)'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='publishing_house',
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ManyToManyField(to='book_shop.PublishingHouse', verbose_name='Издательство'),
        ),
    ]
