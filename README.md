![Workflow badge](https://github.com/petra-khrushcheva/good_deed/actions/workflows/main.yml/badge.svg)

# Good Deed - краудфандинговая платформа
Good Deed - веб-сервис для групповых денежных сборов.  
Доступны эндпойнты для создания и просмотра сборов в пользу зарегистрированных на платформе фондов и создания платежей для сборов.  
Информация сохраняется в базу данных PostgresQL. Реализовано кэширование в Redis.  
Swagger документация доступна по адресу /docs  
***
### Технологии
Python 3.11  
Django 5.0  
Django Rest Framework 3.15  
PostgreSQL  
Redis  
Celery  
SwaggerUI  
***
### Установка
- Клонируйте проект:
```
git clone git@github.com:petra-khrushcheva/good_deed.git
``` 
- Перейдите в директорию good_deed:
```
cd good_deed
``` 
- Cоздайте переменные окружения по [образцу](https://github.com/petra-khrushcheva/good_deed/blob/main/.env.example).
- Запустите Docker-compose:
```
docker compose up
```
- Наполните базу данных моковыми данными:
```
docker exec -it backend sh
cd src
python manage.py populate_database
```