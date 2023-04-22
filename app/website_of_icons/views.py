from django.shortcuts import render
from .models import Icons


def main(request):
    return render(request=request, template_name="main.html")


def home(request):
    if request.method == 'POST':
        print(request.POST.get('search'))
        icons = Icons.objects.get(name=request.POST.get('search'))
        # icons = Icons.objects.all()
    return render(request=request, template_name="icons.html", context={"icons": icons})


def login(request):
    return render(request=request, template_name="login.html")


def registration(request):
    return render(request=request, template_name="signup.html")

# usikzl5j9swGW83B1nWZozLdA04ysQQOT8p8FbOq8hot5lwo
