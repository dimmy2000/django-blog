from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    """User registration form."""

    email = forms.EmailField()

    class Meta:
        """Inner class with metadata."""

        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    """User update form."""

    email = forms.EmailField()

    class Meta:
        """Inner class with metadata."""

        model = User
        fields = [
            "username",
            "email",
        ]


class ProfileUpdateForm(forms.ModelForm):
    """Profile update form."""

    class Meta:
        """Inner class with metadata."""

        model = Profile
        fields = [
            "image",
        ]
