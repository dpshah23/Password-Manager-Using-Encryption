from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('', views.home),
    path('signup', views.signup),
    path('add_new_password', views.addnewpassword),
    path('logout', views.logout),
]