import django_tables2 as tables
from .models import Index

class IndexTable(tables.Table):
    class Meta:
        model = Index
        template_name = "django_tables2/bootstrap.html"
        # fields = ("ipaddress", )
