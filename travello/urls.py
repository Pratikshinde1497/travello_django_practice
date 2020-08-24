from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="Home"),
    path('index.html', views.home, name="Home"),
    path('news.html', views.news, name="news"),

    path('destinations', views.destinations, name="destinations"),
]