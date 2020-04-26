import django_tables2 as tables
from .models import Index
from django_tables2 import A

class IndexTable(tables.Table):
    # export_formats = ['csv', 'json', 'xls', 'xlsx', 'yaml']

    ansible_host = tables.Column(accessor='ansible_host')
    # hw_model = tables.Column(accessor='hw_model')
    hw_bhs = tables.Column(accessor='hw_model.hw_bhs')
    # os_version = tables.Column(accessor='os_version')
    hw_family = tables.Column(accessor='hw_model.hw_family')
    os_bhs = tables.Column(accessor='os_version.os_bhs')
    os_name = tables.Column(accessor='os_version.os_name')
    hw_cve = tables.Column(accessor='hw_model__hardwarepsirt()')
    os_cve = tables.Column(accessor='os_version.hardwarebhs.hardwarepsirt.cve_id')
    is_resolved = tables.Column(accessor='hw_model__hardwarepsirt_test__is_resolved')


    class Meta:
        model = Index
        template_name = "django_tables2/bootstrap.html"
        # fields = ["ipaddress", "cve_id"]
