from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.Genres)
admin.site.register(models.PublishingHouse)
admin.site.register(models.YearPublishing)
admin.site.register(models.Format)