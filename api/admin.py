from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','ISBN','title','author','published','publisher','price','available')
    

admin.site.register(Book,BookAdmin)