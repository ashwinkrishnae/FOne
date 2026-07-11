from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message


def index(request):
    form = MessageForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        message = form.cleaned_data["message"]

        if len(message.strip()) > 8:
            Message.objects.create(username=username, message=message)
            return render(request, "guest/success.html", {"username": username})

        error = "Your message must be longer than 8 characters."

    return render(request, "guest/index.html", {"form": form, "error": error})


def login_view(request):
    if request.session.get("is_admin"):
        return redirect("admin_dashboard")

    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if username == "admin" and password == "admin4196":
            request.session["is_admin"] = True
            return redirect("admin_dashboard")

        error = "Invalid username or password."

    return render(request, "guest/login.html", {"error": error})


def logout_view(request):
    request.session.pop("is_admin", None)
    return redirect("login")


def admin_dashboard(request):
    if not request.session.get("is_admin"):
        return redirect("login")

    messages = Message.objects.order_by("-created_at")
    return render(request, "guest/admin_dashboard.html", {"messages": messages})


def delete_message(request, message_id):
    if not request.session.get("is_admin"):
        return redirect("login")

    if request.method == "POST":
        Message.objects.filter(pk=message_id).delete()

    return redirect("admin_dashboard")


def delete_all_messages(request):
    if not request.session.get("is_admin"):
        return redirect("login")

    if request.method == "POST":
        Message.objects.all().delete()

    return redirect("admin_dashboard")
