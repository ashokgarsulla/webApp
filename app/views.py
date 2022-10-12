from django.shortcuts import HttpResponse, render
from . models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    template = "app/home.html"
    return render(request,template,context)

