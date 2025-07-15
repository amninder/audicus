from __future__ import absolute_import, print_function, unicode_literals

from audicus.models.order import Order
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class OrderSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Order


    closedate = auto_field()
    total_order_value__c = auto_field()
    parent_subscription_id__c = auto_field()
