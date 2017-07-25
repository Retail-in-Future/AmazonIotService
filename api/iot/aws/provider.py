import boto3


class AwsIotProvider(object):
    def __init__(self):
        self._client = boto3.client('iot')

    def list_things(self):
        try:
            return self._client.list_things()
        except:
            return None

    def update_thing(self, thing, data):
        try:
            ret = self._client.update_thing(thingName=thing, attributePayload={'attributes': data, 'merge': True})
            return ret['ResponseMetadata']['HTTPStatusCode'] == 200
        except:
            return False