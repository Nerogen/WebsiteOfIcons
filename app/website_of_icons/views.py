from django.shortcuts import render


def main(request):
    return render(request=request, template_name="main.html")


def home(request):
    return render(request=request, template_name="icons.html")


def login(request):
    return render(request=request, template_name="login.html")


def registration(request):
    return render(request=request, template_name="signup.html")
































# usikzl5j9swGW83B1nWZozLdA04ysQQOT8p8FbOq8hot5lwo