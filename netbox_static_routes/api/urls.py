from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_static_routes'

router = NetBoxRouter()
router.register('static-routes', views.StaticRouteViewSet)

urlpatterns = router.urls
