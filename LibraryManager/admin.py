from django.contrib import admin

from .models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'country']
    list_display = ('name', 'country')
    search_fields = ['name', 'country']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'num_pages')
    search_fields = ['title', 'author__name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
