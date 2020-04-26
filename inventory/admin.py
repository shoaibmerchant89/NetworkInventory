from django.contrib import admin
from .models import *


class HardwareAdmin(admin.ModelAdmin):
    list_display = ('hw_model',)
    list_display_links = ('hw_model',)
    list_filter = ('hw_model',)
    search_fields = ('hw_model',)
    list_per_page = 25

    class Meta:
        model = Hardware

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('os_version',)
    list_display_links = ('os_version',)
    list_filter = ('os_version',)
    search_fields = ('os_version',)
    list_per_page = 25

    class Meta:
        model = Software


class HardwareBhsAdmin(admin.ModelAdmin):
    list_display = ('hw_model', 'hw_bhs', 'hw_family', 'hw_vendor')
    list_display_links = ('hw_model',)
    list_filter = ('hw_model', 'hw_bhs', 'hw_family', 'hw_vendor')
    list_editable = ('hw_bhs',)
    search_fields = ('hw_model','hw_family', 'hw_vendor')
    list_per_page = 25

    class Meta:
        model = HardwareBhs

class HardwarePsirtAdmin(admin.ModelAdmin):
    list_display = ('id', 'hw_model', 'cve_id', 'published_date', 'is_resolved')
    list_display_links = ('id', 'hw_model', 'cve_id')
    list_filter = ('hw_model', 'cve_id')
    list_editable = ('is_resolved',)
    search_fields = ('hw_model',)
    list_per_page = 25

class SoftwareBhsAdmin(admin.ModelAdmin):
    list_display = ('os_version', 'os_bhs', 'os_name', 'os_vendor')
    list_display_links = ('os_version',)
    list_filter = ('os_version', 'os_bhs')
    list_editable = ('os_bhs',)
    search_fields = ('os_version',)
    list_per_page = 25

class SoftwarePsirtAdmin(admin.ModelAdmin):
    list_display = ('id', 'os_version', 'cve_id', 'published_date')
    list_display_links = ('id', 'os_version', 'cve_id')
    list_filter = ('os_version', 'cve_id')
    search_fields = ('os_version',)
    list_per_page = 25

class EmpAdmin(admin.ModelAdmin):
    pass

class SpdwAdmin(admin.ModelAdmin):
    pass

class SpectrumAdmin(admin.ModelAdmin):
    pass

class NetrequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'ipaddress', 'hostname', 'region', 'datacenter', 'cmcs_group', 'vendor', 'type')
    list_display_links = ('id', 'ipaddress', 'hostname', 'region', 'datacenter', 'vendor', 'type')
    list_filter = ('region', 'datacenter')
    list_editable = ('cmcs_group',)
    search_fields = ('ipaddress', 'hostname', 'vendor', 'type')
    list_per_page = 25

class IndexAdmin(admin.ModelAdmin):
    list_display = ('ansible_host', 'hw_model')
    list_display_links = ('ansible_host', 'hw_model')
    # list_filter = ('realtor', 'price')
    # list_editable = ('is_published', 'price')
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(Hardware, HardwareAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(HardwareBhs, HardwareBhsAdmin)
admin.site.register(HardwarePsirt, HardwarePsirtAdmin)
admin.site.register(SoftwareBhs, SoftwareBhsAdmin)
admin.site.register(SoftwarePsirt, SoftwarePsirtAdmin)
# admin.site.register(Emp, EmpAdmin)
# admin.site.register(Spdw, SpdwAdmin)
# admin.site.register(Spectrum, SpectrumAdmin)
# admin.site.register(Netrequest, NetrequestAdmin)
admin.site.register(Index, IndexAdmin)
