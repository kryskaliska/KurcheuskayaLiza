from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('Название книги', max_length=200, db_index=True)
    image = models.ImageField(upload_to='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ManyToManyField(verbose_name='Автор')
    series = models.ManyToManyField(verbose_name='Название серии', default=True)
    genres = models.ManyToManyField(verbose_name='Жанр')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    #year_of_publishing = 
    num_of_pages = models.PositiveIntegerField()


    def __str__(self):
        return self.name


