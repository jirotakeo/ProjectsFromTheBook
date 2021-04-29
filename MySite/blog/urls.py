from django.urls import path
from .views import post_list, post_detail, PostListView, post_share, post_search
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    #path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),
]
