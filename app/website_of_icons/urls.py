from django.urls import path
from .views import main, home, login_render, registration

urlpatterns = [
    path('', main),
    path('home/', home),
    path('home/login/', login_render),
    path('home/registration/', registration)
]
