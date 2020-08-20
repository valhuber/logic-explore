import os
import sys

import sqlalchemy

# import logic_engine.logic

from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
from typing import NewType
import nw.nw_logic.models as models


basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "nw-app/nw.db")
engine = sqlalchemy.create_engine(conn_string)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add Order - works
new_order = models.Order(AmountTotal=0, CustomerId="ALFKI", ShipCity="Richmond",
                         EmployeeId=6, Freight=1)
session.add(new_order)

# OrderDetails - https://docs.sqlalchemy.org/en/13/orm/backref.html
new_item = models.OrderDetail(ProductId=1, Amount=0,
                              Quantity=1, UnitPrice=18,
                              Discount=0)
new_order.OrderDetailList.append(new_item)

session.commit()

print("\nadd_order, completed\n\n")

anOrder = models.Order()  # type: models.Order
