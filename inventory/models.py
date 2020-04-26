from django.db import models
import uuid

class Hardware(models.Model):
    hw_model = models.CharField(primary_key=True, max_length=20, verbose_name='Hardware Model')
    def __str__(self):
        return self.hw_model
    class Meta:
        verbose_name_plural = "Hardware Inventory"

class Software(models.Model):
    os_version = models.CharField(primary_key=True, max_length=20, verbose_name='OS Version')
    def __str__(self):
        return self.os_version
    class Meta:
        verbose_name_plural = "Software Inventory"

# class HardwareBhsQuerySet(models.query.QuerySet):
#     def hwbuy(self):
#         return self.filter(hw_bhs='Buy')
#     def hwcisco(self):
#         return self.filter(hw_vendor='Cisco')
#
# class HardwareBhsManager(models.Manager):
#     def get_queryset(self):
#         return HardwareBhsQuerySet(self.model, using=self.db)
#
#     def hwbuy(self):
#         return self.get_queryset().hwbuy()
#
#     def hwcisco(self):
#         return self.get_queryset().hwcisco()

    # def get_bhs_status(self):
    #     return super(HardwareBhsManager, self).filter(hardware_bhs_status='Buy')

class HardwareBhs(models.Model):

    def get_next():
        return uuid.uuid4()
    def __str__(self):
        return self.hw_model.hw_model

    bhs_choices = [('Buy', 'Buy'), ('Hold', 'Hold'), ('Sell', 'Sell')]
    # hw_family_choices = [('Cisco', 'Cisco'), ('Fortinet', 'Fortinet'), ('F5 Networks', 'F5 Networks')]
    vendor_choices = [('Cisco', 'Cisco'), ('Fortigate', 'Fortigate'), ('F5 Networks', 'F5 Networks')]

    # id = models.UUIDField(primary_key=True, editable=False, default=get_next, auto_created=True, verbose_name='ID')
    hw_model = models.ForeignKey(Hardware, unique=True, on_delete=models.PROTECT, max_length=20, verbose_name='Hardware Model')
    hw_bhs = models.CharField(max_length=5, choices=bhs_choices, verbose_name='Hardware BHS')
    hw_vendor = models.CharField(max_length=20, choices=vendor_choices, verbose_name='Vendor', default='TBD')
    hw_family = models.CharField(max_length=20, verbose_name='Hardware Family', default='TBD')

    # items = HardwareBhsManager()
    # objects = HardwareBhsManager()

    class Meta:
        verbose_name_plural = "Hardware BHS"


class HardwarePsirt(models.Model):
    id = models.AutoField
    hw_model = models.ForeignKey(HardwareBhs, on_delete=models.PROTECT, related_name='hardwarepsirt', verbose_name='Hardware Model')
    cve_id = models.CharField(max_length=20, verbose_name='CVE ID')
    published_date = models.DateTimeField(max_length=20, verbose_name='Published On')
    is_resolved = models.BooleanField(verbose_name='Resolved', default=False)

    def __str__(self):
        return self.cve_id
    class Meta:
        verbose_name_plural = "Hardware PSIRT"


class SoftwareBhs(models.Model):
    def get_next():
        return uuid.uuid4()

    bhs_choices = [('Buy', 'Buy'), ('Hold', 'Hold'), ('Sell', 'Sell')]
    vendor_choices = [('Cisco', 'Cisco'), ('Fortigate', 'Fortigate'), ('F5 Networks', 'F5 Networks')]

    # id = models.UUIDField(primary_key=True, editable=False, default=get_next, auto_created=True, verbose_name='ID')
    os_version = models.ForeignKey(Software, unique=True, on_delete=models.PROTECT, max_length=20, verbose_name='OS Version')
    os_bhs = models.CharField(max_length=5, choices=bhs_choices, verbose_name='OS BHS', default='TBD')
    os_vendor = models.CharField(max_length=20, choices=vendor_choices, verbose_name='Vendor', default='TBD')
    os_name = models.CharField(max_length=20, verbose_name='OS Name', default='TBD')

    def __str__(self):
        return self.os_version.os_version

    class Meta:
        verbose_name_plural = "Software BHS"

class SoftwarePsirt(models.Model):
    id = models.AutoField
    os_version = models.ForeignKey(SoftwareBhs, on_delete=models.PROTECT, verbose_name='OS Version')
    cve_id = models.CharField(max_length=20, verbose_name='CVE ID')
    published_date = models.DateTimeField(max_length=20, verbose_name='Published On')
    class Meta:
        verbose_name_plural = "Software PSIRT"

    def __str__(self):
        return self.os_version.os_version

class Emp(models.Model):
    hardware_model = models.ForeignKey(Hardware, on_delete=models.PROTECT)
    hardware_family = models.CharField(max_length=20, verbose_name='Hardware Family')
    os_version = models.ForeignKey(Software, on_delete=models.PROTECT)
    os_name = models.CharField(max_length=20, verbose_name='OS Name')
    vendor = models.CharField(max_length=20, verbose_name='Vendor')
    class Meta:
        verbose_name_plural = "EMP"

class Spdw(models.Model):
    ipaddress = models.CharField(primary_key=True, unique=True, max_length=15)
    hostname = models.CharField(max_length=50)
    operational_state = models.CharField(max_length=20)
    datacenter = models.CharField(max_length=20)
    region = models.CharField(max_length=4)
    def __str__(self):
        return self.ipaddress
    class Meta:
        verbose_name_plural = "SPDW"


class Spectrum(models.Model):
    ipaddress = models.CharField(primary_key=True, max_length=15, verbose_name='IP Address')
    sdc_name = models.CharField(max_length=60, verbose_name='SDC Name')
    sdc_ip = models.CharField(max_length=15, verbose_name='SDC IP')
    class Meta:
        verbose_name_plural = "Spectrum"


class Netrequest(models.Model):
    id = models.AutoField
    ipaddress = models.CharField(primary_key=True, max_length=15, verbose_name='IP Address')
    hostname = models.CharField(max_length=40, verbose_name='Hostname')
    region = models.CharField(max_length=15, verbose_name='Region')
    datacenter = models.CharField(max_length=15, verbose_name='Data Center')
    cmcs_group = models.CharField(max_length=50, verbose_name='CMCS Group')
    vendor = models.CharField(max_length=30, verbose_name='Vendor')
    type = models.CharField(max_length=20, verbose_name='Type')
    def __str__(self):
        return self.ipaddress
    class Meta:
        verbose_name_plural = "Netrequest"


class Index(models.Model):
    ansible_host = models.CharField(primary_key=True, unique=True, max_length=15, verbose_name='Ansible Host')
    hw_model = models.ForeignKey(HardwareBhs, to_field='hw_model', on_delete=models.PROTECT, verbose_name='Hardware Model')
    os_version = models.ForeignKey(SoftwareBhs, to_field='os_version', on_delete=models.PROTECT, verbose_name='OS Version', default='TBD')
    def __str__(self):
        return self.ansible_host
    class Meta:
        verbose_name_plural = "Index"

# class IndexFilter(FilterSet):
#     class Meta:
#         model = Index
#         fields = ['ansible_host', 'hw_model', 'os_version']