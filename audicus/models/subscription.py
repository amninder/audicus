from __future__ import absolute_import, print_function, unicode_literals
import datetime as dt

import sqlalchemy as sa
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from audicus.constants.db import STATUS_ACTIVE, STATUS_CANCELLED, STATUS_ON_HOLD

from .db import db
from .mixins import PrimaryKeyMixin


class Subscription(PrimaryKeyMixin, db.Model):
    __tablename__ = "subscriptions"

    end_date = sa.Column("end_date__c", sa.Integer, nullable=True)
    start_date = sa.Column("start_date__c", sa.Integer, nullable=False)

    billing_interval = sa.Column("billing_interval__c",
                                 sa.String,
                                 nullable=False)
    next_payment_date = sa.Column("next_payment_date__c",
                                  sa.Integer,
                                  nullable=True)
    recurring_amount = sa.Column("recurring_amount__c",
                                 sa.Integer,
                                 nullable=True)
    status = sa.Column("status__c", sa.String, nullable=False)

    orders = relationship("Order", back_populates="subscription")

    def __repr__(self):
        return f"<Subscription(id={self.id})"

    @hybrid_property
    def is_on_hold(self):
        return self.status == STATUS_ON_HOLD

    @hybrid_property
    def is_cancelled(self):
        return self.status == STATUS_CANCELLED

    @hybrid_property
    def is_active(self):
        return self.status == STATUS_ACTIVE

    @hybrid_property
    def is_recurring(self):
        return self.recurring_amount is not None

    @hybrid_property
    def end_dt(self):
        if not self.end_date:
            return None
        return dt.datetime.fromtimestamp(self.end_date/1000)

    @hybrid_property
    def start_dt(self):
        return dt.datetime.fromtimestamp(self.start_date/1000)
