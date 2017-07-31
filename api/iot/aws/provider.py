import boto3
import json


class AwsIotProvider(object):
    def __init__(self):
        self._client = boto3.client('iot-data')

    def update_thing(self, thingName, data):
        try:
            body = {"state": {"desired": data}}
            ret = self._client.update_thing_shadow(thingName=thingName, payload=bytes(json.dumps(body), 'utf-8'))
            return ret['ResponseMetadata']['HTTPStatusCode'] == 200
        except:
            return False

    def get_thing(self, thingName):
        return self._client.get_thing_shadow(thingName=thingName);
