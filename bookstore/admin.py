from django.contrib import admin

# Здесь регистрируем созданные модели bookstore и Author
from .models import Book , Author , Subscription
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Subscription)
