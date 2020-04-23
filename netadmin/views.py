from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'netadmin/dashboard.html')


def tables(request):
    return render(request, 'netadmin/tables.html')


def flot(request):
    return render(request, 'netadmin/flot.html')


def morris(request):
    return render(request, 'netadmin/morris.html')


def forms(request):
    return render(request, 'netadmin/forms.html')


def panels_wells(request):
    return render(request, 'netadmin/panels_wells.html')


def buttons(request):
    return render(request, 'netadmin/buttons.html')


def notifications(request):
    return render(request, 'netadmin/notifications.html')


def typography(request):
    return render(request, 'netadmin/typography.html')


def icons(request):
    return render(request, 'netadmin/icons.html')


def grid(request):
    return render(request, 'netadmin/grid.html')


def blank(request):
    return render(request, 'netadmin/blank.html')


def login(request):
    return render(request, 'netadmin/login.html')
