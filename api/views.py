from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.iot.aws.provider import AWSIotProvider


class ThingsViewSet(viewsets.ViewSet):
    aWSIotProvider = AWSIotProvider()

    @detail_route(methods=['get'], url_name='things', url_path='things')
    def list_things(self,request,*args, **kwargs):
        return Response(self.aWSIotProvider.list_things())
