# Api-social-net

>API для проекта social-net.

Стек: Python v3.9, Django, DRF.

#### Как запустить проект:

+ клонируем репозиторий `git clone`
`https://github.com/BeerBellyWell/api_social-net.git`
+ переходим в него `cd api_social-net`
    + разворачиваем виртуальное окружение
    `python3 -m venv env` (Windows: `python -m venv env`)
    + активируем его
    `source env/bin/activate` (Windows: `source env/scripts/activate`)
    + устанавливаем зависимости из файла requirements.txt
    `pip install -r requirements.txt`
+ выполняем миграции
`python3 manage.py migrate` (Windows: `python manage.py migrate`)
+ запускаем проект
`python3 manage.py runserver` (Windows: `python manage.py runserver).

# Инструкции и примеры

>Основные эндпойнты `/api/v1/`:
+ /posts/ 
+ /follow/ 
+ /posts/1/comments/ 
+ /posts/1/comments/1/ 
+ /groups/

