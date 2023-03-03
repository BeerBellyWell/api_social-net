# api_final
api final

Это  для ятуб.

Установка:
    1. Установить виртуальное окружение: python -m venv venv
    2. Активировать: source venv/Script/activate
    3. Установить зависимости: pip install -r requiremets.txt
    4. Выполнить миграции: python manage.py migrate
    5. Запустить проект: python manage.py runserver

Примеры Api:
    http://127.0.0.1:8000/api/v1/posts/
    http://127.0.0.1:8000/api/v1/follow/
    http://127.0.0.1:8000/api/v1/posts/1/comments/
    http://127.0.0.1:8000/api/v1/posts/1/comments/1/
    http://127.0.0.1:8000/api/v1/groups/
