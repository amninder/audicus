from sqlalchemy.orm import declared_attr
import sqlalchemy as sa


class TableNameMxin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class PrimaryKeyMixin:
    id = sa.Column(sa.Integer, primary_key=True)
