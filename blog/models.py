from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """Database model of user's post in blog."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Inner class for adding the metadata to the model."""

        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        """Class instance representation."""
        return self.title

    def get_absolute_url(self):
        """Set the absolute path to the post."""
        return reverse("post-detail", kwargs={"pk": self.pk})
