from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Client


class ClientListView(ListView):
    model = Client
    paginate_by = 10


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
