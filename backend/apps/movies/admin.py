from django.contrib import admin
from .models import Movie
class PostAdmin(admin.ModelAdmin):
     list_display = ['name','release_type','rating','release_type']
admin.site.register(Movie,PostAdmin)
# Register your models here.
