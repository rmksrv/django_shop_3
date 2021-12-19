from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index"),
    path("page/<slug:slug>", views.GenericPageDetailView.as_view(), name="page-detail"),
]
