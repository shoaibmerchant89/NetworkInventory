from django.contrib import admin
from .models import *

class HardwareBhsAdmin(admin.ModelAdmin):
    list_display = ('hardware_model', 'hardware_bhs_status')
    list_display_links = ('hardware_model',)
    list_filter = ('hardware_model', 'hardware_bhs_status')
    list_editable = ('hardware_bhs_status',)
    search_fields = ('hardware_model',)
    list_per_page = 25

class HardwarePsirtAdmin(admin.ModelAdmin):
    # list_display = ('id', 'hardware_model', 'cve_id', 'published_date')
    # list_display_links = ('id', 'hardware_model', 'cve_id')
    # list_filter = ('hardware_model', 'cve_id')
    # search_fields = ('hardware_model',)
    list_per_page = 25

class SoftwareBhsAdmin(admin.ModelAdmin):
    list_display = ('os_version', 'software_bhs_status')
    list_display_links = ('os_version',)
    list_filter = ('os_version', 'software_bhs_status')
    list_editable = ('software_bhs_status',)
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
    list_display = ('ansible_host',)
    list_display_links = ('ansible_host',)
    # list_filter = ('realtor', 'price')
    # list_editable = ('is_published', 'price')
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(HardwareBhs, HardwareBhsAdmin)
admin.site.register(HardwarePsirt, HardwarePsirtAdmin)
admin.site.register(SoftwareBhs, SoftwareBhsAdmin)
admin.site.register(SoftwarePsirt, SoftwarePsirtAdmin)
# admin.site.register(Emp, EmpAdmin)
# admin.site.register(Spdw, SpdwAdmin)
# admin.site.register(Spectrum, SpectrumAdmin)
admin.site.register(Netrequest, NetrequestAdmin)
admin.site.register(Index, IndexAdmin)
