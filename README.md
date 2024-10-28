# Blog API

## Запуск проекта

1. Клонируйте репозиторий.
2. Создайте `.env` в корне проекта, используя `.env.example` для примера, и убедитесь, что `DB_HOST` и `DB_PORT` не изменены:
    ```env
    DB_HOST=db
    DB_PORT=5432
    ```
3. Запустите приложение с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```
4. Примените миграции:
    ```bash
    docker-compose exec web python manage.py migrate
    ```
5. Загрузите моковые данные в PostgreSQL:
    ```bash
    docker-compose exec web python src/manage.py insert_mock_data
    ```

## Эндпоинты

- `GET /posts/?page=int&limit=int`: Получение всех постов с пагинацией.
- `GET /posts/{id}/`: Получение конкретного поста.
- `POST /posts/`: Создание нового поста.
- `PUT /posts/{id}/`: Обновление существующего поста.
- `DELETE /posts/{id}/`: Удаление поста.
- `GET /posts/search/?search=term`: Поиск по названию или содержимому.
- `GET /posts/statistics/{user_id}/`: Статистика постов по пользователю.
