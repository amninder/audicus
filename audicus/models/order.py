from __future__ import absolute_import, print_function, unicode_literals

import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, relationship

from .db import db
from .mixins import PrimaryKeyMixin


class Order(PrimaryKeyMixin, db.Model):
    __tablename__ = "orders"


    closedate = sa.Column(sa.Integer, nullable=False)
    total_order_value = sa.Column("total_order_value__c", sa.Integer, nullable=False)

    subscription_id = mapped_column("parent_subscription_id__c", sa.ForeignKey("subscriptions.id"))
    subscription = relationship("Subscription", back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id})>"
