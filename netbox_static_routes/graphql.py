from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


class StaticRouteType(NetBoxObjectType):

    class Meta:
        model = models.StaticRoute
        fields = '__all__'

class Query(ObjectType):
    static_route = ObjectField(StaticRouteType)
    static_route_list = ObjectListField(StaticRouteType)
    
schema = Query