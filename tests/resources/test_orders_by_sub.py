from __future__ import absolute_import, print_function, unicode_literals
import json

import mock
import requests
from mock import MagicMock
from tests import BaseTest
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD
from audicus.schema.get_subscription import (
    FetchSubscription,
    FetchSubscriptionSchema,
)
from audicus.schema.subscription_schema import SubscriptionSchema


class TestSubscriptions(BaseTest):

    def test_post_invalid_payload(self):
        """Test case to test post to raise error for invalid request body"""
        response = self.client.post(
            "/subscriptions/",
            json=json.dumps({"name": "this"}),
        )
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual({"message": "Not a valid request body."},
                             response.get_json())

    @mock.patch("requests.get")
    def test_post_serializable_body_invalid_response(self, mocked_get):
        """Test case to test throw error when invalid data received"""
        mocked_response = MagicMock()
        mocked_response.status_code = 200
        mocked_response.json.return_value = [{"this": "that"}]
        mocked_get.return_value = mocked_response

        obj = FetchSubscription(from_page=1, to_page=4, per_page=100)
        schema = FetchSubscriptionSchema()
        response = self.client.post("/subscriptions/", json=schema.dumps(obj))

        self.assertDictEqual({"message": "Invalid data received."},
                             response.get_json())
        self.assertEqual(400, response.status_code)

    @mock.patch("requests.get")
    def test_post_serializable_body_valid_response(self, mocked_get):
        """Test case to test invalid data received"""
        sub1 = SubscriptionFactory(status=STATUS_ACTIVE)
        sub2 = SubscriptionFactory(status=STATUS_ACTIVE)

        sub3 = SubscriptionFactory(status=STATUS_CANCELLED)
        sub4 = SubscriptionFactory(status=STATUS_CANCELLED)

        sub5 = SubscriptionFactory(status=STATUS_ON_HOLD)
        sub6 = SubscriptionFactory(status=STATUS_ON_HOLD)

        schema = SubscriptionSchema()

        mocked_response = MagicMock()
        mocked_response.status_code = 200
        mocked_response.json.return_value = {
            "subscriptions": [
                schema.dump(sub1),
                schema.dump(sub2),
                schema.dump(sub3),
                schema.dump(sub4),
                schema.dump(sub5),
                schema.dump(sub6),
            ]
        }
        mocked_get.return_value = mocked_response

        obj = FetchSubscription(from_page=1, to_page=1, per_page=100)
        schema = FetchSubscriptionSchema()
        response = self.client.post("/subscriptions/", json=schema.dumps(obj))
        expected_response = {
            'status_count': {
                'active': 2,
                'cancelled': 2,
                'on-hold': 2
            }
        }
        self.assertDictEqual(expected_response, response.get_json())
