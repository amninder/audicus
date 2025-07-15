from __future__ import absolute_import, print_function, unicode_literals

from audicus.models.subscription import Subscription
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class SubscriptionSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Subscription


    end_date__c = auto_field()
    start_date__c = auto_field()

    billing_interval__c = auto_field()
    next_payment_date__c = auto_field()
    recurring_amount__c = auto_field()
    status__c = auto_field()
