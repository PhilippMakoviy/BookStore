#Hello DeepLongevity!
#Это приложение Книжный Магазин

#Задание написано на языке Python 3.0, просьба не судить строго =) 

#Код находится здесь же в свободном доступе - в ветке master

#Используемый стэк: rest_framework, djoser, rest_framework_simplejwt

#Немного информации для проверяющего по пунктам:

#я писал данную программу в PyCharm и тестил в  Postman и Boomerang
#При необходимости для доступа к админской панели, пройти по адресу: http://127.0.0.1:8000/admin/
Логин: Admin
Пароль: Admin

Реализовать методы api:
1)POST создать нового пользователя (простейшее ручное создание, не надо заморачиваться регистрацией)

Запрос для регистрации нового пользователя:

POST http://127.0.0.1:8000/accounts/register/

В запросе передать(username,password,email)

2)GET выдать список пользователей

GET http://127.0.0.1:8000/api/userslist/

3)- GET выдать информацию по конкретному пользователю

GET http://127.0.0.1:8000/api/userslist/1 

где 1 это id конкретного пользователя


4)POST прошла оплата у пользователя

POST http://127.0.0.1:8000/api/subscription/

В запросе необходимо передать
username
period
status

Если статус "ok" то происходит оплата подписки, если другое значение, то отказ оплаты
В поле "period" необходимо передать "month" или "year"

5)GET выдать пользователю список книг (для этого подписка не нужна)

GET http://127.0.0.1:8000/api/books/


6)- GET выдать пользователю информацию по конкретной книге (для этого нужна подписка)

При запросе GET http://127.0.0.1:8000/api/books/1 (где 1 это id книги)
Система откажет в доступе

Я реализовал механизм авторизации через JWT токены.

Для получения токена нужно например через postman сделать запрос (вместе с запросом также отправить username и password):

http://127.0.0.1:8000/auth/jwt/create

В полученном ответе от сервера забрать токен access

Необходимо выбрать тип авторизации Bearer Token вставить в поле Token полученный на предыдущем шаге ключ
Далее сделать снова запрос http://127.0.0.1:8000/api/books/1

Система выдаст информацию по конкретной книге(Токен действует 14 дней, далее можно продлить его, снова сделав JWT запрос)

Спасибо за интересное задание! =)


С уважением, Маковий Филипп


