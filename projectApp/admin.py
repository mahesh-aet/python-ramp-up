from django.contrib import admin
from .models import Album, GeekModel, Musician

# Register your models here.
admin.site.register(GeekModel)
admin.site.register(Musician)
admin.site.register(Album)