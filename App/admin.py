from django.contrib import admin
from .models import Book

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ['title', 'author']

admin.site.register(Book, PostAdmin)
