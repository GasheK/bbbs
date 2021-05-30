from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityListViewSet

router = DefaultRouter()
router.register(r'cities', CityListViewSet, 'city_list')


urlpatterns = [
    path('', include(router.urls)),
]
