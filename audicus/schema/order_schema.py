from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from audicus.models.order import Order


class OrderSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Order


    closedate = auto_field()
    total_order_value__c = auto_field()
    parent_subscription_id__c = auto_field()
