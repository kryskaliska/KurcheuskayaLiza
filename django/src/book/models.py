from django.db import models
from book_shop_ref.models import Series, Genres, YearPublishing, Format

# Create your models here.

class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=200,
        db_index=True
    )
    #image = models.ImageField(
    #    verbose_name='Изображение',
    #    upload_to='',
    #    blank=True
    #)
    author = models.ManyToManyField(
        'book_shop_ref.Author',
        verbose_name='Автор(ы)'
    )
    price = models.DecimalField(
        verbose_name='Цена (BYN)',
        max_digits=10,
        decimal_places=2
    )
    available = models.BooleanField(
        verbose_name='Доступно к заказу',
        default=True
    )
    stock = models.PositiveIntegerField(
        verbose_name='Количество в наличии'
    )
    age = models.ForeignKey(
        'book_shop_ref.Age',
        on_delete=models.PROTECT,
        verbose_name='Возрастные ограничения',
        default='5',
        related_name='books'
    )
    series = models.ForeignKey(
        'book_shop_ref.Series',
        on_delete=models.PROTECT,
        verbose_name='Название серии',
        default=True,
        related_name='books'
    )
    genres = models.ForeignKey(
        'book_shop_ref.Genres',
        on_delete=models.PROTECT,
        verbose_name='Жанр',
        related_name='books'
    )
    num_of_pages = models.PositiveIntegerField(
        verbose_name='Количество страниц'
    )
    book_format = models.ManyToManyField(
        'book_shop_ref.Format',
        verbose_name='Формат книги'
    )
    type_binding = models.ManyToManyField(
        'book_shop_ref.Binding',
        verbose_name='Тип переплёта'
    )
    publishing_house = models.ManyToManyField(
        'book_shop_ref.PublishingHouse',
        verbose_name='Издательство'
    )
    year_of_publishing = models.ManyToManyField(
        'book_shop_ref.YearPublishing',
        verbose_name='Год издания'
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=15,
        default='',
        unique=True
    )
    created = models.DateTimeField(
        verbose_name='Дата внесения',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    
    
    def __str__(self):
       # return f'Название книги: {self.name}, aвтор(ы): {self.author.name}, цена(BYN): {self.price}, возрастные ограничения: {self.age}, название серии: {self.series.name}, жанр: {self.genres.name},  количество страниц: {self.num_of_pages}, город: {self.publishing_house.city}, издательство: {self.publishing_house.name}, год издания: {self.year_of_publishing}, формат: {self.book_format}, '
       return self.name