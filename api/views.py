from rest_framework import viewsets, status
from rest_framework.response import Response
from api.iot.aws.provider import AwsIotProvider


class ThingsViewSet(viewsets.ViewSet):
    awsIotProvider = AwsIotProvider()

    def update_thing(self, request, thing):
        if not self.awsIotProvider.update_thing(thing,request.data):
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_200_OK)