from django.urls import path
from . views import home,PostCreateView,PostDetailView
urlpatterns = [
    path('',home,name="apphome"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]