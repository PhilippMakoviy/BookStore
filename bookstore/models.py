from django.db import models
from django.contrib.auth.models import User
# Здесь создаем модели

#непосредственно класс книг
class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    #owner = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#Класс подписка, через который мы будем производить оплату
class Subscription(models.Model):

    username = models.CharField(max_length=20)
    status = models.CharField(max_length=5)
    period = models.CharField(max_length=5)


    def __str__(self):
         return self.username


#в качестве дополнения класс Автор книг
class Author(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
         return self.name
