from django.urls import path
from . import views

# URL Configuration for the app. The first argument is the URL path users' browser will visit.
urlpatterns = [
	path('hello/', views.say_hello)
]
