from .forms import UserRegisterForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your Account has been created! You are now able to Log In"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def home(request):
    return HttpResponse("You have successfully Logged In!")
