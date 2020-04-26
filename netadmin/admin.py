from django.contrib import admin
from .models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nationality')

    class Meta:
        model = authors

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'isbn', 'author')

    class Meta:
        model = books

class FansAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

    class Meta:
        model = fans

admin.site.register(authors, AuthorAdmin)
admin.site.register(books, BooksAdmin)
admin.site.register(fans, FansAdmin)

