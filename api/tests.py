import json

import mock
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from api.iot.aws.provider import AwsIotProvider


def get_thing():
    return {
        'state': {
            'desired': {'attribute1': 'zhongguo'},
            'delta': {'attribute1': 'zhongguo'}},
        'metadata': {
            'desired': {'attribute1': {'timestamp': 1501209577}}
        },
        'version': 14, 'timestamp': 1501480404
    }


class ThingsApiTest(TestCase):
    def setUp(self):
        self.client = RequestsClient();
        self.base_url = "http://localhost:8000/api"

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_update_thing_attribute_by_thing_name(self, mock_update_thing):
        mock_update_thing.return_value = True
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )

        assert status.HTTP_200_OK == response.status_code

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_return_service_unavailable__when_update_failed(self, mock_update_thing):
        mock_update_thing.return_value = False
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )
        assert status.HTTP_503_SERVICE_UNAVAILABLE == response.status_code

    @mock.patch.object(AwsIotProvider, 'get_thing')
    def test_should_return_thing_device_shadow_by_thing_name(self, mock_list_thing):
        mock_list_thing.return_value = get_thing()
        thingName = 'Green_Lights01'

        response = self.client.get(url=self.base_url + '/things/' + thingName)
        json_str = str(response.content, encoding="utf-8")
        json_obj = json.loads(json_str)

        assert status.HTTP_200_OK == response.status_code
        assert 'zhongguo' == json_obj['state']['desired']['attribute1']

    @mock.patch.object(AwsIotProvider, 'get_thing')
    def test_should_service_unavailable_when_get_failed(self,mock_list_thing):
        mock_list_thing.return_value = None
        thingName = 'Green_Lights01'

        response = self.client.get(url=self.base_url + '/things/' + thingName)
        assert status.HTTP_503_SERVICE_UNAVAILABLE == response.status_code

