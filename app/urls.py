from django.urls import path
from . views import UserPostListView,PostCreateView,PostDetailView,PostListView
urlpatterns = [
    path('',PostListView.as_view(),name="apphome"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]