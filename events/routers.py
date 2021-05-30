from rest_framework.routers import Route, DefaultRouter


class CustomRouter(DefaultRouter):
    """
    A router to allow delete object without lookup.
    """
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create',
                'delete': 'destroy'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
    ]
