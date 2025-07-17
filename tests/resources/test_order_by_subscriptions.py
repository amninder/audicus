from __future__ import absolute_import, print_function, unicode_literals
import datetime as dt
import math

import mock
from dateutil.relativedelta import relativedelta
from mock import MagicMock
from tests import BaseTest
from tests.factories.order_factory import OrderFactory
from tests.factories.subscription_factory import SubscriptionFactory

from audicus.schema.order_schema import OrderSchema


class TestSubscriptions(BaseTest):

    @mock.patch("requests.get")
    def test_get(self, mock_get):
        """Get average days of orders"""
        order_schema = OrderSchema()
        subscription = SubscriptionFactory()

        today = dt.datetime.today()

        month_ago = relativedelta(months=1)
        order_2_ts = (today - month_ago)

        two_months_ago = relativedelta(months=2)
        order_3_ts = (today - two_months_ago)

        order1 = OrderFactory(subscription=subscription, closedate=math.floor(order_3_ts.timestamp() * 1000))
        order2 = OrderFactory(subscription=subscription, closedate=math.floor(order_2_ts.timestamp() * 1000))
        order3 = OrderFactory(subscription=subscription, closedate=math.floor(today.timestamp() * 1000))

        mocked_response = MagicMock()
        mocked_response.status_code = 200
        mocked_response.json.return_value = {
            "count": 3,
            "next_page": 2,
            "page": 1,
            "total_count": 3,
            "orders": [
                order_schema.dump(order1),
                order_schema.dump(order2),
                order_schema.dump(order3),
            ]
        }
        mock_get.return_value = mocked_response

        response = self.client.get("/subscriptions/49303/orders/")
        expected_value = {
            "average_days": 30
        }
        self.assertDictEqual(expected_value, response.json)
