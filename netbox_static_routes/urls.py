from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('static-routes/', views.StaticRouteListView.as_view(), name='staticroute_list'),
    path('static-routes/add/', views.StaticRouteEditView.as_view(), name='staticroute_add'),
    path('static-routes/edit/', views.StaticRouteBulkEditView.as_view(), name='staticroute_bulk_edit'),
    path('static-routes/delete/', views.StaticRouteBulkDeleteView.as_view(), name='staticroute_bulk_delete'),
    path('static-routes/<int:pk>', views.StaticRouteView.as_view(), name='staticroute'),
    path('static-routes/<int:pk>/edit/', views.StaticRouteEditView.as_view(), name='staticroute_edit'),
    path('static-routes/<int:pk>/delete/', views.StaticRouteDeleteView.as_view(), name='staticroute_delete'),
    path('static-routes/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='staticroute_changelog', kwargs={
        'model': models.StaticRoute
    }),
)
