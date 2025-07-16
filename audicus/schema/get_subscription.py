from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from typing import Union

from marshmallow import Schema, fields, post_load


@dataclass
class SubPayload:
    count: int
    next_page: int
    page: int
    total_count: int


class GetSubscription(Schema):
    count = fields.Integer()
    next_page = fields.Integer()
    page = fields.Integer()
    total_count = fields.Integer()

    @post_load
    def create_sub(self, data, **kwargs):
        return SubPayload(**data)


@dataclass
class FetchSubscription:
    from_page: int
    per_page: Union[None, int]
    to_page: int


class FetchSubscriptionSchema(Schema):
    from_page = fields.Integer(required=True)
    per_page = fields.Integer(load_default=100)
    to_page = fields.Integer(required=True)

    @post_load
    def create_order(self, data, **kwargs):
        return FetchSubscription(**data)
