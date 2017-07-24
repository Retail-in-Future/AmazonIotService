import boto3


class AWSIotProvider:

    def __init__(self):
        self.client = boto3.client('iot')

    def list_things(self):
        return self.client.list_things()
        pass

    pass
