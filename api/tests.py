import json

import mock
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from api.iot.aws.provider import AwsIotProvider


def list_things():
    return {
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
        'things': [{'thingName': 'Green_Lights01', 'thingTypeName': 'Light', 'attributes': {}, 'version': 2},
                   {'thingName': 'Green_Lights01', 'thingTypeName': 'Light', 'attributes': {}, 'version': 2}]}


class ThingsApiTest(TestCase):
    def setUp(self):
        self.client = RequestsClient();
        self.base_url = "http://localhost:8000/api"

    @mock.patch.object(AwsIotProvider, 'list_things')
    def test_should_get_thing_shadow(self, mock_list_things):
        mock_list_things.return_value = list_things()

        response = self.client.get(url=self.base_url + '/things')
        json_str = str(response.content, encoding="utf-8")
        json_Obj = json.loads(json_str)

        assert status.HTTP_200_OK == response.status_code
        self.assertTrue(mock_list_things.called)
        assert 2 == len(json_Obj['things'])

    @mock.patch.object(AwsIotProvider, 'list_things')
    def test_should_return_service_unavailable_when_happened_exception(self, mock_list_things):
        mock_list_things.return_value = None

        response = self.client.get(self.base_url + '/things')

        assert status.HTTP_503_SERVICE_UNAVAILABLE == response.status_code

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_update_thing_attribute_by_thing_name(self, mock_update_thing):
        mock_update_thing.return_value = True
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )

        assert status.HTTP_200_OK == response.status_code

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_return_service_unavaibal__when_update_failed(self,mock_update_thing):
        mock_update_thing.return_value = False
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )
        assert status.HTTP_503_SERVICE_UNAVAILABLE == response.status_code
