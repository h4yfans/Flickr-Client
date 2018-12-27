from django.urls import path
from .views import index, UserFavoriteListView, post_user_likes

app_name = 'tags'

urlpatterns = [
    path('', index, name='index'),
    path('likes/', UserFavoriteListView.as_view(), name='favorites'),
    path('post-like/', post_user_likes, name='post-like'),

]
