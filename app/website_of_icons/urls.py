from django.urls import path
from .views import main, home, login, registration

urlpatterns = [
    path('', main),
    path('home/', home),
    path('home/login/', login),
    path('home/registration/', registration)
]
