import mock
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from api.iot.aws.provider import AwsIotProvider


class ThingsApiTest(TestCase):
    def setUp(self):
        self.client = RequestsClient();
        self.base_url = "http://localhost:8000/api"

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_update_thing_attribute_by_thing_name(self,mock_update_thing):
        mock_update_thing.return_value = True
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )

        assert status.HTTP_200_OK == response.status_code

    @mock.patch.object(AwsIotProvider, 'update_thing')
    def test_should_return_service_unavaibal__when_update_failed(self, mock_update_thing):
        mock_update_thing.return_value = False
        attribute = {'color': 'Green'}

        response = self.client.post(url=self.base_url + '/things/Green_Lights01', json=attribute, )
        assert status.HTTP_503_SERVICE_UNAVAILABLE == response.status_code
