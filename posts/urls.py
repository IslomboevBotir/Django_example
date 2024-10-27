from django.urls import path
from posts import views as post_views

urlpatterns = [
    path('', post_views.PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', post_views.PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('search/', post_views.search_posts, name='post-search'),
    path('statistics/<int:user_id>/', post_views.posts_statistics, name='post-statistics'),
]
