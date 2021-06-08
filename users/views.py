from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ProfileUpdateForm
from .forms import UserRegisterForm
from .forms import UserUpdateForm


def register(request):
    """User registration view."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You are able now to log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request,
        "users/register.html",
        {"form": form},
    )


@login_required
def profile(request):
    """User profile view."""
    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(
        request,
        "users/profile.html",
        context,
    )
