from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from audicus.models.order import Order


class OrderSchema(SQLAlchemySchema):

    class Meta:
        load_instance = True
        model = Order

    id = auto_field()
    closedate = auto_field()
    total_order_value = auto_field(data_key="total_order_value__c")
    subscription_id = auto_field(data_key="parent_subscription_id__c")
