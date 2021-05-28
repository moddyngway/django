from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about-us"),
    path('fumo', views.fumo, name="fumo"),
    path('create', views.create, name="create"),
]
