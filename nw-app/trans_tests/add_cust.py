import os
import sys

import sqlalchemy

import app.models
# import logic_engine.logic
import nw_logic.models
from nw_app import logic  # see .env file (or pycharm Add Content Roots)
import typing
import nw_app.app.models as models


basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "nw.db")
engine = sqlalchemy.create_engine(conn_string)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add a Customer - works
new_cust = models.Customer(Id="$$New Cust1", )
session.add(new_cust)
session.commit()

print("\nhello worldDB, completed\n\n")

anOrder = models.Order()  # type: models.Order
