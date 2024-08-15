## Реализация API социальной сети на Django Rest Framework

### Описание
Моя попытка реализовать API для небольшой социальной сети, по функционалу напоминающую Reddit

### Мотивация
Проект написан в рамках изучения Django Rest Framework

### Установка и запуск
1. Клонирование репозитория
~~~shell
git clone https://github.com/BobaUbisoft17/social_network
~~~

2. Необходимо создать ```.env``` файл и внести ключ для шифрования данных в переменную DJANGOSECRETKEY
    + Можно получить ключ выполив команду в консоли
    ~~~shell
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ~~~
    + Или на подобных [сайтах](https://djecrety.ir/)

3. Запуск
~~~shell
docker-compose up --build
~~~

### Документация API

+ Добавление новых пользователей
    http://localhost:8000/auth/users

+ Получение JWT-токена
    http://localhost:8000/auth/jwt/create

+ Документация по основным ручкам
    http://localhost:8000/api_v1/swagger/