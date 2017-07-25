import boto3


class AwsIotProvider(object):
    def __init__(self):
        self._client = boto3.client('iot')

    def list_things(self):
        try:
            return self._client.list_things()
        except:
            return None