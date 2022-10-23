from django.contrib import admin
from .models import Book

class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'pages', 'release_year']
    list_filter = ['release_year', 'author']
    search_fields = ['title', 'author']
    list_per_page = 10


admin.site.register(Book, AdminBook)