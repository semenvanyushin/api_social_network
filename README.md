# ЯндексПрактикум - Спринт 9 - Проект «API для Yatube». 
# Python-разработчик (бекенд) (Яндекс.Практикум)

### Описание
API для Yatube - это проект социальной сети, который имеет функционал: публикация постов, комментирование поста, подписки на авторов постов.

### Технологии
Python 3.7.9, Django 2.2.16, Django Rest Framework 3.12.4, JWT + Djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/semenvanyushin/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3.7 -m venv venv
```
или
```
py -3.7 -m venv venv
```

Для MacOS или Linux:
```
source env/bin/activate
```
Для Windows:
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна только в режиме чтения.

Cписок всех постов:

```
GET api/v1/posts/
```
При указании параметров limit и offset выдача работает с пагинацией

Получение поста по id:

```
GET api/v1/posts/{id}/
```

Список доступных групп:
```
GET api/v1/groups/
```

Получение информации о группе по id:
```
GET api/v1/groups/{id}/
```

Все комментарии к посту:
```
GET api/v1/{post_id}/comments/
```

Получение комментария к посту по id:
```
GET api/v1/{post_id}/comments/{id}/
```

### Примеры работы с API для авторизованных пользователей
Авторизованные пользователи могут: создавать посты, комментировать их, подписываться на авторов постов.
Пользователи могут изменять/удалять контент, если являются его автором.

Создания поста:

```
POST /api/v1/posts/
```
в body { "text": "string", "image": "string", "group": 0 }

Изменение поста:

```
PUT /api/v1/posts/{id}/
```
в body { "text": "string", "image": "string", "group": 0 }

Изменение части поста:

```
PATCH /api/v1/posts/{id}/
```
в body { "text": "string", "image": "string", "group": 0 }

Удаление поста:

```
DEL /api/v1/posts/{id}/
```

Доступ к эндпоинту /api/v1/follow/ доступен только для авторизованных пользователей.

Список своих подписок на авторов:

```
GET /api/v1/follow/
```
в body {"user": "string", "following": "string"}

Подписка на автора:

```
POST /api/v1/follow/
```
в body {"following": "string"}
