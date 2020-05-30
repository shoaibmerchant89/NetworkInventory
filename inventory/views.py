from django.shortcuts import render
from django.views.generic import ListView

from .models import Index
from .models import Netrequest
from .tables import IndexTable
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from django.views.generic import TemplateView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# Create your views here.

# class IndexListView(ListView):
#     model = Index
#     template_name = 'NetworkInventory/base.html'
class homeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = {'context': 'context is being rendered!'}
        return context

# class IndexListView(ExportMixin,SingleTableView):
#     model = Index
#     table_class = IndexTable
#     template_name = 'NetworkInventory/base.html'

# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = IndexTable
#     model = Index
#     template_name = "NetworkInventory/base.html"
#     filter = IndexFilter
#
# def product_list(request):
#     filter = ProductFilter(request.GET, queryset=Product.objects.all())
#     return render(request, 'my_app/template.html', {'filter': filter})