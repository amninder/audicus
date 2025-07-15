from __future__ import absolute_import, print_function, unicode_literals

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD

from .db import db
from .mixins import PrimaryKeyMixin


class Subscription(PrimaryKeyMixin, db.Model):
    __tablename__ = "subscriptions"


    end_date = sa.Column("end_date__c", sa.Integer, nullable=True)
    start_date = sa.Column("start_date__c", sa.Integer, nullable=False)

    billing_interval = sa.Column("billing_interval__c", sa.String, nullable=False)
    next_payment_date = sa.Column("next_payment_date__c", sa.Integer, nullable=True)
    recurring_amount = sa.Column("recurring_amount__c", sa.Integer, nullable=True)
    status = sa.Column("status__c", sa.String, nullable=False)

    orders = relationship("Order", back_populates="subscription")

    def __repr__(self):
        return f"<Subscription(id={self.id})"

    def isOnHole(self):
        return self.status== STATUS_ON_HOLD

    def isCancelled(self):
        return self.status== STATUS_CANCELLED


    def isActive(self):
        return self.status == STATUS_ACTIVE
