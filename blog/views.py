from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Post


def home(request):
    """Home page view."""
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    """List of posts view."""

    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    """List of posts for certain user view."""

    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        """Get QuerySet for all posts of certain user."""
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    """Post details view."""

    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create post view."""

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """Override the form_valid method to set the logged user as the post author."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update post view."""

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """Override the form_valid method to set the logged user as the post author."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Check that author of post is updating it."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Post delete view."""

    model = Post
    success_url = "/"

    def test_func(self):
        """Check that author of post is deleting it."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """About page view."""
    return render(request, "blog/about.html", {"title": "About"})
