from django.urls import path

from . import views

app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="client-list"),
    path("client/filter", views.ClientFilterView.as_view(), name="client-filter"),
    path(
        "client/detail/<slug:slug>",
        views.ClientDetailView.as_view(),
        name="client-detail",
    ),
    path(
        "client/update/<slug:slug>",
        views.ClientUpdateView.as_view(),
        name="client-update",
    ),
    path("client/new", views.ClientCreateView.as_view(), name="client-create"),
    path(
        "payment/detail/<int:pk>",
        views.PaymentDetailView.as_view(),
        name="payment-detail",
    ),
    path(
        "payment/update/<int:pk>",
        views.PaymentUpdateView.as_view(),
        name="payment-update",
    ),
    path("payment/new", views.PaymentCreateView.as_view(), name="payment-create"),
]
