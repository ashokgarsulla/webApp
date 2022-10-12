from django.shortcuts import HttpResponse, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from . models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    template = "app/home.html"
    return render(request,template,context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'app/post_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)