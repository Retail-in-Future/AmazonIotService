from django.http import HttpResponse
from api.iot.aws.provider import AWSIotProvider

def index(request):
    aWSIotProvider = AWSIotProvider();
    return HttpResponse(aWSIotProvider.list_things());
