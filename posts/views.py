from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Count

from .models import Post
from .serializer import PostSerializer
from .pagination import CustomPagination


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def search_posts(request):
    query = request.query_params.get('search', None)
    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.none()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def posts_statistics(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    monthly_posts = (
        Post.objects
        .filter(user=user)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    total_posts = sum(item['count'] for item in monthly_posts)
    total_months = len(monthly_posts)
    avg_posts_per_month = total_posts / total_months if total_months > 0 else 0

    return Response({
        "average_posts_per_month": avg_posts_per_month,
        "monthly_posts": monthly_posts  # Для проверки, сколько постов было по месяцам
    })
