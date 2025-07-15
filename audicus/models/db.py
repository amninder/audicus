# from flask_sqlalchemy import SQLAlchemy;
import sqlalchemy as sa
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)


Base = declarative_base()
# db = SQLAlchemy(model_class=Base)

engine = sa.create_engine("sqlite://", echo=True)
Session = sessionmaker(engine)
