from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from audicus.models.subscription import Subscription


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
