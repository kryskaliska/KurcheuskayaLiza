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
    book_format = models.ForeignKey(
        'book_shop_ref.Format',
        on_delete=models.PROTECT,
        verbose_name='Формат книги',
        related_name='books'
    )
    publishing_house = models.ManyToManyField(
        'book_shop_ref.PublishingHouse',
        verbose_name='Издательство'
    )
    year_of_publishing = models.ManyToManyField(
        'book_shop_ref.YearPublishing',
        verbose_name='Год издания'
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
        return f'{self.name} {self.author.name} {self.series.name} {self.genres.name} {self.publishing_house.name} {self.num_of_pages} {self.book_format} {self.year_of_publishing}'