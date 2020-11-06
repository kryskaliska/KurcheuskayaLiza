from django.db import models

# Create our models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Фамилия И.О.',
        max_length=200,
    )

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name='Книжная серия',
        max_length=200,
    )

    def __str__(self):
       return self.name

class Genres(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=200,
    )

    def __str__(self):
        return self.name

class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=200,
    )

    def __str__(self):
        return self.name

#class Customer(models.Model):
#    
#class Manager(models.Model):
#    
#class Admin(models.Model): 
    

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
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )
    author = models.ManyToManyField(
        'book_shop_ref.Author',
        verbose_name='Автор(ы)'
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name='Название серии',
        default=True
    )
    genres = models.ForeignKey(
        Genres,
        on_delete=models.PROTECT,
        verbose_name='Жанр'
    )
    publishing_house = models.ManyToManyField(
        'book_shop_ref.PublishingHouse',
        verbose_name='Издательство'
    )
    #year_of_publishing =
    stock = models.PositiveIntegerField(
        verbose_name='Количество в наличии'
    )
    available = models.BooleanField(
        verbose_name='Доступно к заказу',
        default=True
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
    num_of_pages = models.PositiveIntegerField(
        verbose_name='Количество страниц'
    )
    
    
    def __str__(self):
        return f'{self.name} {self.author.name} {self.series.name} {self.genres.name} {self.publishing_house.name} {self.num_of_pages}'


