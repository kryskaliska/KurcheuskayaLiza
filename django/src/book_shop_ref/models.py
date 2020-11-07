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

class City(models.Model):
    name = models.CharField(
        verbose_name='Город',
        max_length=50,
        default='Москва'
    )

class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=200,
    )
    city = models.ForeignKey(
        'book_shop_ref.City',
        on_delete=models.PROTECT,
        verbose_name='Город',
        related_name='publishing_houses',
        default='Москва'
    )

    def __str__(self):
        return f'Издательство: {self.name}, город: {self.city}'

class YearPublishing(models.Model):
    year = models.CharField(
        verbose_name='Год издания',
        max_length=4,
    )

    def __str__(self):
       return self.year

class Format(models.Model):
    size = models.CharField(
        verbose_name='Формат книги',
        max_length=10,
    )

    def __str__(self):
        return self.size
#class Customer(models.Model):
#    
#class Manager(models.Model):
#    
#class Admin(models.Model): 
    



