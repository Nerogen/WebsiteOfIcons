from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from .models import Icons


class Register(View):
    template_name = './signup.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users/shortener')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def logout_user(request):
    logout(request)
    return redirect('/users/shortener')


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


def login_render(request):
    return render(request=request, template_name="login.html")


def registration(request):
    return render(request=request, template_name="signup.html")

# usikzl5j9swGW83B1nWZozLdA04ysQQOT8p8FbOq8hot5lwo
