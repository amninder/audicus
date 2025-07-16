from __future__ import absolute_import, print_function, unicode_literals

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from audicus.models.subscription import Subscription


class SubscriptionSchema(SQLAlchemySchema):

    class Meta:
        load_instance = True
        model = Subscription
        auto_flush = True


    id = auto_field()
    end_date = auto_field(data_key="end_date__c")
    start_date = auto_field(data_key="start_date__c")

    billing_interval = auto_field(data_key="billing_interval__c")
    next_payment_date = auto_field(data_key="next_payment_date__c")
    recurring_amount = auto_field(data_key="recurring_amount__c")
    status = auto_field(data_key="status__c")
