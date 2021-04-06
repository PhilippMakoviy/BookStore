from django.urls import path
from .views import BookView,SingleBookView,UsersList,SingleUserView,SubscriptionView

#from bookstore.views import HomeView, ContactsView, LoginView

# Cоздаем URL с которого пользователь будет получать доступ к методу
app_name = "books"

#непосрдественно адреса относящиеся к приложению(переадресация с test_django.urls)
urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
    path('userslist/', UsersList.as_view()), #name="userslist"),
    path('userslist/<int:pk>', SingleUserView.as_view()),
    path('subscription/', SubscriptionView.as_view())


    #path('accounts/login/', LoginView.as_view(), name="login")
    #path('accounts/profile/', ProfilePage.as_view(), name="profile")
]