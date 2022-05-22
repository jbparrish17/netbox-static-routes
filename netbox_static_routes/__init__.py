from extras.plugins import PluginConfig
from .version import __version__

class NetBoxStaticRoutesConfig(PluginConfig):
    name = 'netbox_static_routes'
    verbose_name = 'Netbox Static Routes'
    description = 'Manage static routes in Netbox'
    version = __version__
    author = 'Joshua Parrish'
    author_email = 'jbparrish17@gmail.com'
    base_url = 'static-routes'
    required_settings = []
    min_version = '3.2.0'
    max_version = '3.2.99'
    default_settings = {}

config = NetBoxStaticRoutesConfig
