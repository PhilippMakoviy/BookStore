"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path

from bookstore.views import ProfilePage, RegisterView,LoginView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    # path to djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),


    path('api/', include('bookstore.urls')),
    path('accounts/login/', LoginView.as_view(), name="login"),
    re_path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile")

]


