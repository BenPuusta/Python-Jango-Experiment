from django.urls import path

from . import views
from . import testyviews

urlpatterns = [
    path("", views.index, name="index"),
    #path("", testyviews.extraTestyTest, name="extraTestyTest")
]