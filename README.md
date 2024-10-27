# Blog API

## Запуск проекта
1. Клонируйте репозиторий.
2. Создайте .env в корне проекта используя для примера .env.example не изменяя значения DB_HOST и DB_PORT
2. Запустите `docker-compose up --build` для сборки и запуска приложения.
3. Примените миграции: `docker-compose exec web python manage.py migrate`
4. Загружите моковые данные в PostgreSQL `docker-compose exec web python manage.py insert_mock_data`

## Эндпоинты
- `GET /posts/`: Получение всех постов с пагинацией.
- `GET /posts/{id}/`: Получение конкретного поста.
- `POST /posts/`: Создание нового поста.
- `PUT /posts/{id}/`: Обновление существующего поста.
- `DELETE /posts/{id}/`: Удаление поста.
- `GET /posts/search/?search=term`: Поиск по названию или содержимому.
- `GET /posts/statistics/{user_id}/`: Статистика постов по пользователю.

