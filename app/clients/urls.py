from django.urls import path

from . import views

app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="list"),
    path("detail/<slug:client_id>", views.ClientDetailView.as_view(), name="detail"),
    path("update/<slug:client_id>", views.ClientUpdateView.as_view(), name="update"),
    path("new", views.ClientCreateView.as_view(), name="creates"),
]
