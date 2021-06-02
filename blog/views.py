from django.shortcuts import render

posts = [
    {
        "author": "dimmy2000",
        "title": "Post #1",
        "content": "Hello World!",
        "date_posted": "June 1, 2021",
    },
    {
        "author": "John Doe",
        "title": "Post #2",
        "content": "This is the second post content",
        "date_posted": "June 2, 2021",
    },
]


def home(request):
    """Home page view."""
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    """About page view."""
    return render(request, "blog/about.html")
