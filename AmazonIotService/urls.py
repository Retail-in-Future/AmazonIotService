"""AmazonIotService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, Route

from api.views import ThingsViewSet

router = DefaultRouter()
router.register('', ThingsViewSet, 'api')
router.routes.append(
    Route(
        url=r'^api/things/(?P<thing>[a-zA-Z0-9_]+)$',
        name='thing_resource',
        mapping={
            'post': 'update_thing',
            'get': 'get_thing',
            'delete': 'delete_thing'
        },
        initkwargs={}
    )
)

urlpatterns = [url(r'', include(router.urls))]
