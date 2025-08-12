"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from plants.views import PlantsViewSet
from rest_framework import routers

# from plants.views import PlantsApiList, PlantsApiUpdate, PlantsApiDetailView

class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=False,
            initkwargs={'suffix': 'Detail'}
        )
    ]


# router = routers.SimpleRouter()
router = MyCustomRouter()
router.register(r'plants', PlantsViewSet, basename='plants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/plantslist/', PlantsViewSet.as_view({'get': 'list'})),
    # path('api/v1/plantslist/<int:pk>/', PlantsViewSet.as_view({'put': 'update'})),


]
