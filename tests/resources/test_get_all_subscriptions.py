from __future__ import absolute_import, print_function, unicode_literals

import mock
from mock import MagicMock
from tests import BaseTest
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD
from audicus.schema.subscription_schema import SubscriptionSchema


class TestSubscriptions(BaseTest):

    @mock.patch("requests.get")
    def test_get_all_subscriptions(self, mocked_get):
        """Test case to get the list of all subscriptions"""
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
            ],
            "page": 1,
            "count": 6,
            "total_count": 6,
            "next_page": 2,
        }
        mocked_get.return_value = mocked_response
        response = self.client.get("/")
        expected_response = {
            'status_count': {
                'active': 2,
                'cancelled': 2,
                'on-hold': 2
            }
        }
        self.assertDictEqual(expected_response, response.json)
