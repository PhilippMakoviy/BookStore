from rest_framework import serializers
from .models import Book,Subscription
from django.contrib.auth.models import User

#Ниже приведены все используемые для вывода информации сериалайзеры с необходимыми полями

class SingleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'body', 'author_id')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('username','status', 'period')

    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id' , 'username', 'email')

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=120)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



