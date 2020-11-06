from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.Genres)
admin.site.register(models.PublishingHouse)