from django.test import TestCase
from mock import MagicMock
from rest_framework.test import APIClient
from rest_framework import status
import boto3



class ApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.base_url = 'http://127.0.0.1:8000/'

    def should_get_thing_shadow(self):
        client = boto3.client('iot')
        client.list_things = MagicMock(return_value={
            'ResponseMetadata': {'RequestId': 'ed7b7d21-6de9-11e7-a746-293614f4a237', 'HTTPStatusCode': 200,
                                 'HTTPHeaders': {'content-type': 'application/json', 'content-length': '182',
                                                 'connection': 'keep-alive', 'date': 'Fri, 21 Jul 2017 07:55:13 GMT',
                                                 'x-amzn-requestid': 'ed7b7d21-6de9-11e7-a746-293614f4a237',
                                                 'access-control-allow-origin': '*',
                                                 'x-amzn-trace-id': 'Root=1-5971b361-34f0cb1e2e519cba44cdd9bd',
                                                 'x-cache': 'Miss from cloudfront',
                                                 'via': '1.1 a0c37528226f4371674e076c912931a9.cloudfront.net (CloudFront)',
                                                 'x-amz-cf-id': 'ly3ANpYC1hMlOJr_9jtsuDNpNasgIdldjljwwtkngbsl0qTwWpI9UA=='},
                                 'RetryAttempts': 0},
            'things': [{'thingName': 'Green_Lights01', 'thingTypeName': 'Light', 'attributes': {}, 'version': 2},{'thingName': 'Green_Lights01', 'thingTypeName': 'Light', 'attributes': {}, 'version': 2}]},);

        response = self.client.get(self.base_url + 'things');
        assert 2 == len(client.list_things()['things']);
