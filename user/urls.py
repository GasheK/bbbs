from django.urls import path
from .views import UsersViewSet, CityViewSet


urlpatterns = [
    #path(r'v1/cites/', CityViewSet.as_view({'get': 'list'})),
    path(r'', UsersViewSet.as_view({'get': 'list',
                                               'patch': 'partial_update',
                                               'put': 'update'})),
]