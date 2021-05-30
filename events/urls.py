from django.urls import include, path
from .routers import CustomRouter
from .views import EventViewSet, EventParticipantViewSet, MainViewSet

router = CustomRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'event-participants', EventParticipantViewSet, basename='event-participant')
router.register(r'main', MainViewSet, basename='main')


urlpatterns = [
    path('', include(router.urls)),
]
