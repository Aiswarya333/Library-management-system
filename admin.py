
from django.contrib import admin
from lib.models import User, Book

class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title","author","published_date","availability"]
admin.site.register(Book, BookModelAdmin)
admin.site.register(User)