from django.shortcuts import render

from .models import Post


def home(request):
    """Home page view."""
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


def about(request):
    """About page view."""
    return render(request, "blog/about.html")
