from __future__ import absolute_import, print_function, unicode_literals
import math
import posixpath

import requests
from flask import request
from flask_restful import Resource, abort
from marshmallow.exceptions import ValidationError

from audicus.constants import BASE_API_URL
from audicus.schema.get_subscription import FetchSubscriptionSchema
from audicus.utils.get_path import getpath
from audicus.utils.guard import guard
from audicus.utils.stats import DF


class OrdersBySub(Resource):

    def get(self, sub_id, order_id):
        return {"url": 2}


class GetSubscriptions(Resource):

    def post(self):
        """Post data to fetch subscriptions"""
        data = []
        schema = FetchSubscriptionSchema()
        subscription_params = guard(lambda: schema.load(request.json), against=(ValidationError,))
        if not subscription_params:
            abort(400, message="Not a valid request body.")
            return
        for i in range(subscription_params.from_page, subscription_params.to_page + 1):
            url = posixpath.join(BASE_API_URL, "subscriptions/", str(i))
            resp = requests.get(url, params={"per_page": subscription_params.per_page})
            body = resp.json()

            resp_subscription = guard(lambda: getpath(body, "subscriptions"), against=(TypeError))
            if resp_subscription == None:  # noqa
                abort(400, message="Invalid data received.")
                return
            data.extend(getpath(body, "subscriptions"))
        df = DF(data)
        return {"status_count": df.status_count}


class AllSubscriptions(Resource):
    BASE_URL = "https://jungle.audicus.com/v1/coding_test/subscriptions/"

    def get(self):
        all_subscriptions = []
        first_url = posixpath.join(self.BASE_URL, "1")
        resp = requests.get(first_url)
        data = resp.json()
        count = getpath(data, "count")
        total_count = getpath(data, "total_count")
        all_subscriptions.extend(getpath(data, "subscriptions"))
        total_pages = math.ceil(total_count/count)
        for i in range(2, total_pages + 1):
            url = posixpath.join(self.BASE_URL, str(i))
            resp = requests.get(url)
            all_subscriptions.extend(getpath(resp.json(), "subscriptions"))

        df = DF(all_subscriptions)
        return {"status_count": df.status_count}
