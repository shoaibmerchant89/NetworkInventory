from django.shortcuts import render
from django.views.generic import ListView

from .models import Index
from .models import Netrequest
from .tables import IndexTable
from django_tables2 import SingleTableView
# Create your views here.

# class NetrequestListView(ListView):
#     model = Netrequest
#     template_name = 'tutorial/Netrequest.html'

class IndexListView(SingleTableView):
    model = Index
    table_class = IndexTable
    template_name = 'NetworkInventory/base.html'
