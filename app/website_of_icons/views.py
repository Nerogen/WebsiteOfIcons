from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from django.shortcuts import render
from .models import Icons


def main(request):
    return render(request=request, template_name="main.html")


def get(request):
    context = {
        'form': UserCreationForm()
    }
    return render(request, context)


def home(request):
    if request.method == "POST":
        icons = Icons.objects.all()
        subject_matter = request.POST.get('subject_matter')
        icons = [icon for icon in icons if subject_matter == str(icon)]
        return render(request=request, template_name="icons.html", context={"icons": icons})
    else:
        icons = request.GET.get('subject_matter')
        print(icons)
        return render(request=request, template_name="icons.html")


def login(request):
    return render(request=request, template_name="login.html")


def registration(request):
    return render(request=request, template_name="signup.html")

# usikzl5j9swGW83B1nWZozLdA04ysQQOT8p8FbOq8hot5lwo
