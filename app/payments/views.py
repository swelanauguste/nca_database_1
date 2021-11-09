from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from .models import Payment


class PaymentListView(ListView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    fields = "__all__"


class PaymentCreateView(CreateView):
    model = Payment
    fields = "__all__"


class PaymentDetailView(DetailView):
    model = Payment
