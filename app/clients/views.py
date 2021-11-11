from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from .models import Client, Payment


class PaymentCreateView(CreateView):
    model = Payment
    fields = "__all__"


class PaymentDetailView(DetailView):
    model = Payment


class PaymentListView(ListView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    fields = "__all__"
    template_name_suffix = "_update_form"


class ClientFilterView(ListView):
    model = Client
    paginate_by = 10

    def get_queryset(self):
        queryset = Client.objects.all()
        q = self.request.GET.get("q")
        # start_date_created_at = self.request.GET.get("start_date_created_at")
        # end_date_created_at = self.request.GET.get("end_date_created_at")
        # print(
        #     "start_date_created_at",
        #     start_date_created_at,
        #     "end_date_created_at",
        #     end_date_created_at,
        #     "q",
        #     q,
        # )
        if q:
            queryset = queryset.filter(
                Q(client__icontains=q)
                | Q(client_id__icontains=q)
                | Q(email__icontains=q)
                | Q(national_insurance_id__icontains=q)
            ).distinct()
        # if start_date_created_at and end_date_created_at:
        #     queryset = queryset.filter(
        #         Q(dob__gte=start_date_created_at) & Q(dob__lte=end_date_created_at)
        #     ).distinct()

        return queryset


class ClientListView(ListView):
    model = Client
    paginate_by = 5


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    template_name_suffix = "_update_form"
