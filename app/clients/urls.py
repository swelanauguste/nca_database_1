from django.urls import path

from . import views

app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="list"),
    path("filter", views.ClientFilterView.as_view(), name="filter"),
    path("detail/<slug:slug>", views.ClientDetailView.as_view(), name="detail"),
    path("update/<slug:slug>", views.ClientUpdateView.as_view(), name="update"),
    path("new", views.ClientCreateView.as_view(), name="creates"),
]
