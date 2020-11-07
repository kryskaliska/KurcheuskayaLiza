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

    def __str__(self):
        return self.name

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
    FORMAT_CHOICES = [
        ('1', '84×108/32'),
        ('2', '60×90/16'),
        ('3', '60×90/32'),
        ('4', '70×108/32'),
        ('5', '70×90/32'),
        ('6', '75×90/16'),
        ('7', '70×90/16'),
        ('8', '70×90/8'),
        ('9', '84×108/16'),
        ('10', '70×100/64'),
    ]
    size = models.CharField(
        verbose_name='Формат книги',
        choices=FORMAT_CHOICES,
        max_length=10,
        default='1'
    )

    def __str__(self):
        return self.size

class Binding(models.Model):
    BINDING_CHOICES = [
        ('1', '7БЦ'),
        ('2', '7Б'),
        ('3', '7Т'),
        ('4', 'КБС'),
        ('5', 'ШКС'),
        ('6', 'Брошюровка на пружину'),
        ('7', 'Брошюровка скобой'),
        ('8', 'Интегральный'),
        ('9', 'Болты'),
    ]
    type_binding = models.CharField(
        verbose_name='Тип переплёта',
        choices=BINDING_CHOICES,
        max_length=30,
        default='1'
    )

    def __str__(self):
        return self.type_binding

class Age(models.Model):
    AGE_CHOICES = [
        ('1', '0+'),
        ('2', '6+'),
        ('3', '12+'),
        ('4', '16+'),
        ('5', '18+'),
    ]
    age = models.CharField(
        verbose_name='Возрастные ограничения',
        choices=AGE_CHOICES,
        max_length=3,
        default='5'
    )

    def __str__(self):
        return self.age   


#class Customer(models.Model):
#    
#class Manager(models.Model):
#    
#class Admin(models.Model): 
    



