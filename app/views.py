from django.shortcuts import HttpResponse, get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.models import User
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

class PostListView(ListView):
    model = Post
    template_name = 'app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'app/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'

