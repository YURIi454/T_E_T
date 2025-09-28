# T E T 
###### Tracking Everything Today
#### Курсовой проект Django REST API трекер привычек,подключён Telegram-бот и напоминания через Celery.

## Документация API
Доступна по адресам:
+ Swagger UI: http://localhost:8000/api/docs/swagger/
+ Redoc: http://localhost:8000/api/docs/redoc/

## Тестирование
```python manage.py test```

## Структура 
+ users/ — пользователь
+ tracker/ — привычки
+ telega/ — интеграция с Telegram
+ config/ — настройки проекта
+ requirements.txt — список зависимостей