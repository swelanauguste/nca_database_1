from django.urls import path

from . import views

app_name = "payments"


urlpatterns = [
    path("", views.PaymentListView.as_view(), name="payment-list"),
    path("create", views.PaymentCreateView.as_view(), name="payment-create"),
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
]
