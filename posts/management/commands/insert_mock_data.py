from django.core.management.base import BaseCommand
from django.db import connection
from django.utils import timezone


class Command(BaseCommand):
    help = 'Insert mock data into the auth_user and posts tables using raw SQL'

    def handle(self, *args, **kwargs):
        current_time = timezone.now()

        users_sql = """
        INSERT INTO auth_user (username, password, email, is_staff, is_active, is_superuser, date_joined, first_name, last_name)
        VALUES
            ('user1', 'pbkdf2_sha256$216000$abcdef$1234567890abcdef1234567890abcdef', 'user1@example.com', true, true, true, %s, 'User', 'One'),
            ('user2', 'pbkdf2_sha256$216000$abcdef$1234567890abcdef1234567890abcdef', 'user2@example.com', true, true, true, %s, 'User', 'Two')
        ON CONFLICT (username) DO NOTHING;
        """

        posts_sql = """
        INSERT INTO posts (user_id, title, content, created_at, updated_at)
        VALUES
            (1, 'Пост 1 от user1', 'Содержимое поста 1 для user1', %s, %s),
            (1, 'Пост 2 от user1', 'Содержимое поста 2 для user1', %s, %s),
            (1, 'Пост 3 от user1', 'Содержимое поста 3 для user1', %s, %s),
            (1, 'Пост 4 от user1', 'Содержимое поста 4 для user1', %s, %s),
            (1, 'Пост 5 от user1', 'Содержимое поста 5 для user1', %s, %s),
            (2, 'Пост 1 от user2', 'Содержимое поста 1 для user2', %s, %s),
            (2, 'Пост 2 от user2', 'Содержимое поста 2 для user2', %s, %s),
            (2, 'Пост 3 от user2', 'Содержимое поста 3 для user2', %s, %s),
            (2, 'Пост 4 от user2', 'Содержимое поста 4 для user2', %s, %s),
            (2, 'Пост 5 от user2', 'Содержимое поста 5 для user2', %s, %s)
        ON CONFLICT DO NOTHING;
        """

        with connection.cursor() as cursor:
            cursor.execute(users_sql, [current_time, current_time])
            timestamps = [current_time, current_time] * 10  # For 10 rows of posts
            cursor.execute(posts_sql, timestamps)

        self.stdout.write(self.style.SUCCESS('Mock data inserted successfully'))
