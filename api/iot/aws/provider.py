import boto3
import json


class AwsIotProvider(object):
    def __init__(self):
        self._client = boto3.client('iot-data')

    def update_thing(self, thing, data):
        try:
            body = {"state": {"desired": data}}
            ret = self._client.update_thing_shadow(thingName=thing, payload=bytes(json.dumps(body), 'utf-8'))
            return ret['ResponseMetadata']['HTTPStatusCode'] == 200
        except:
            return False
