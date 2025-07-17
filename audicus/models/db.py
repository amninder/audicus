# from flask_sqlalchemy import SQLAlchemy;
from __future__ import absolute_import, print_function, unicode_literals

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base


Base = declarative_base()
db = SQLAlchemy(model_class=Base)
