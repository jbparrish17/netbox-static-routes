from netbox.views import generic
from . import filtersets, forms, models, tables

class StaticRouteView(generic.ObjectView):
    queryset = models.StaticRoute.objects.all()

class StaticRouteListView(generic.ObjectListView):
    queryset = models.StaticRoute.objects.all()
    table = tables.StaticRouteTable
    filterset = filtersets.StaticRouteFilterSet
    filterset_form = forms.StaticRouteFilterForm

class StaticRouteEditView(generic.ObjectEditView):
    queryset = models.StaticRoute.objects.all()
    form = forms.StaticRouteForm

class StaticRouteBulkEditView(generic.BulkEditView):
    queryset = models.StaticRoute.objects.all()
    table = tables.StaticRouteTable
    form = forms.StaticRouteBulkEditForm
    filterset = filtersets.StaticRouteFilterSet

class StaticRouteDeleteView(generic.ObjectDeleteView):
    queryset = models.StaticRoute.objects.all()

class StaticRouteBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StaticRoute.objects.all()
    table = tables.StaticRouteTable

