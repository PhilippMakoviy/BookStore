from django.shortcuts import render

# Метод через который можно просмотреть все книги и Авторов
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book,Subscription
from .serializers import BookSerializer,UserSerializer,RegisterSerializer,SingleBookSerializer,SubscriptionSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView

#ниже последние изменения
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser

#Здесь представлены все вьюшки, с помощью которых мы делаем запрос и получаем ответ

#Просмотр книг
class BookView(ListModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request):
        book = request.data.get('book')
        # Create an article from the above data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book_saved.title)})


#просмотр подписки
class SubscriptionView(ListModelMixin, GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request):
        new_subscript = request.data.get('subscription')
        # Create an article from the above data
        serializer = SubscriptionSerializer(data=new_subscript)
        if serializer.is_valid(raise_exception=True):
            subscript_saved = serializer.save()
        if subscript_saved.status == 'ok':
            return Response({"Оплата для пользователя {} прошла успешно".format(subscript_saved.username + ' сроком на ' + subscript_saved.period)})
        else:
            return Response({"Ошибка оплаты, проверьте данные вашей банковской карты"})

#просмотр отдельной книги
class SingleBookView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = SingleBookSerializer

#просмотр списка пользователей
class UsersList(ListModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#просмотр отдельного пользователя
class SingleUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    template_name = "registration/login.html"
    #для логина систему в графическом режиме (использовал для отладки)
    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)
    #для создания пользователя с помощью API
    def post(self, request):
        user = request.data.get('user')

        serializer = RegisterSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username)})

#для регистрации пользователя
class RegisterView(APIView):
    def post(self, request):
        user = request.data.get('user')
        print(user)

        serializer = RegisterSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username)})

#использовался для отладки
class ProfilePage(APIView):
    template_name = "registration/profile.html"

    def get(self, request, format=None):
        return Response("Здравствуйте! Добро пожаловать в библиотеку!")
