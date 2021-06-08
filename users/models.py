from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    """Database model of user profile in blog."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics")

    class Meta:
        """Inner class for adding metadata to model."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Class instance representation."""
        return f"{self.user.username} Profile"

    def save(self):
        """Redefinition of parent's class save method."""
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
