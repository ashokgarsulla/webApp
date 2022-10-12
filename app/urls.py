from django.urls import path
from . views import home,PostCreateView
urlpatterns = [
    path('',home,name="apphome"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]