from . import views
from django.urls import path
from .views import HomeView, AddView
urlpatterns = [
    path('',AddView.as_view(), name="adding"),
]