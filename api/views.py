from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.iot.aws.provider import AwsIotProvider


class ThingsViewSet(viewsets.ViewSet):
    awsIotProvider = AwsIotProvider()

    @detail_route(methods=['get'], url_name='things', url_path='things')
    def list_things(self, request, *args, **kwargs):
        things_response = self.awsIotProvider.list_things()
        if things_response is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({'things': things_response['things']},status=status.HTTP_200_OK)