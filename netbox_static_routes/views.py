from netbox.views import generic
from . import forms, models, tables

class StaticRouteView(generic.ObjectView):
    queryset = models.StaticRoute.objects.all()

class StaticRouteListView(generic.ObjectListView):
    queryset = models.StaticRoute.objects.all()
    table = tables.StaticRouteTable

class StaticRouteEditView(generic.ObjectEditView):
    queryset = models.StaticRoute.objects.all()
    form = forms.StaticRouteForm

class StaticRouteDeleteView(generic.ObjectDeleteView):
    queryset = models.StaticRoute.objects.all()
    