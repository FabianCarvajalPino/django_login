from django.urls import path
from . import views

urlpatterns = [
    path('', views.logreg),
    path('login', views.login),
    path('registration', views.reg),
    path('success', views.success),
    path('logout', views.logout)

]