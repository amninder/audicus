from __future__ import absolute_import, print_function, unicode_literals

import sqlalchemy as sa
from sqlalchemy.orm import declared_attr


class TableNameMxin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class PrimaryKeyMixin:
    id = sa.Column(sa.Integer, primary_key=True)
