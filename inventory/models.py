from django.db import models
import uuid

# class hardware_software(models.Model):
#     hardware_model = models.CharField(max_length=20, verbose_name='hardware_model')
#     os_version = models.CharField(max_length=20, verbose_name='os_version')
#     class Meta:
#         unique_together = ('hardware_model', 'os_version')
class HardwareBhs(models.Model):
    def get_next():
        return uuid.uuid4()

    id = models.UUIDField(editable=False, default=get_next, auto_created=True, verbose_name='ID')
    hardware_model = models.CharField(primary_key=True, max_length=20, verbose_name='Hardware Model')
    choices = [
        ('Buy', 'Buy'),
        ('Hold', 'Hold'),
        ('Sell', 'Sell')
    ]
    hardware_bhs_status = models.CharField(max_length=5, choices=choices, verbose_name='Hardware BHS')

    def __str__(self):
        return self.hardware_model

    class Meta:
        verbose_name_plural = "Hardware BHS"

class HardwarePsirt(models.Model):
    # id = models.AutoField
    # hardware_model = models.ForeignKey(HardwareBhs, on_delete=models.PROTECT, related_name='hardwaremodel_psirt', verbose_name='Hardware Model')
    # cve_id = models.CharField(max_length=20, verbose_name='CVE ID')
    # published_date = models.DateTimeField(max_length=20, verbose_name='Published On')
    # def __str__(self):
    #     return self.hardware_model.hardware_model
    # def __unicode__(self):
    #     return u'' + self.hardware_model
    class Meta:
        verbose_name_plural = "Hardware PSIRT"

class SoftwareBhs(models.Model):
    def get_next():
        return uuid.uuid4()

    id = models.UUIDField(editable=False, default=get_next, auto_created=True, verbose_name='ID')
    os_version = models.CharField(primary_key=True, max_length=20)
    choices = [
        ('Buy', 'Buy'),
        ('Hold', 'Hold'),
        ('Sell', 'Sell')
    ]
    software_bhs_status = models.CharField(max_length=5, choices=choices, verbose_name='Software BHS')
    class Meta:
        verbose_name_plural = "Software BHS"

class SoftwarePsirt(models.Model):
    id = models.AutoField
    os_version = models.ForeignKey(SoftwareBhs, on_delete=models.PROTECT, verbose_name='OS Version')
    cve_id = models.CharField(max_length=20, verbose_name='CVE ID')
    published_date = models.DateTimeField(max_length=20, verbose_name='Published On')
    class Meta:
        verbose_name_plural = "Software PSIRT"

class Emp(models.Model):
    hardware_model = models.ForeignKey(HardwareBhs, on_delete=models.PROTECT)
    hardware_family = models.CharField(max_length=20, verbose_name='Hardware Family')
    os_version = models.ForeignKey(SoftwareBhs, on_delete=models.PROTECT)
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
    hardware_model = models.ForeignKey(HardwareBhs, on_delete=models.PROTECT, verbose_name='Hardware Model')
    os_version = models.ForeignKey(SoftwareBhs, on_delete=models.PROTECT, verbose_name='Software Model')
    def __str__(self):
        return self.ansible_host
    class Meta:
        verbose_name_plural = "Index"
