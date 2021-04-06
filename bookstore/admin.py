from django.contrib import admin

# Здесь регистрируем созданные модели bookstore и Author
from .models import Book , Author
admin.site.register(Book)
admin.site.register(Author)
