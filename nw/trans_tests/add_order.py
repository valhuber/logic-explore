import os
import sys

import sqlalchemy
from sqlalchemy import event
from sqlalchemy.orm import session

# import logic_engine.logic

from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
from typing import NewType
import nw.nw_logic.models as models


def my_before_commit(a_session):
    print("before commit!")


def add_order(a_session: session):
    # Add Order - works
    new_order = models.Order(AmountTotal=0, CustomerId="ALFKI", ShipCity="Richmond",
                             EmployeeId=6, Freight=1)
    a_session.add(new_order)

    # OrderDetails - https://docs.sqlalchemy.org/en/13/orm/backref.html
    new_item1 = models.OrderDetail(ProductId=1, Amount=0,
                                   Quantity=1, UnitPrice=18,
                                   Discount=0)
    new_order.OrderDetailList.append(new_item1)

    new_item2 = models.OrderDetail(ProductId=2, Amount=0,
                                   Quantity=2, UnitPrice=18,
                                   Discount=0)
    new_order.OrderDetailList.append(new_item2)

    a_session.commit()

    print("\nadd_order, completed\n\n")


def upd_order(a_session: session):
    john = a_session.query(models.Order).filter(models.Order.id == -1).one()
    print("\nupd_order, completed\n\n")


basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "nw-app/nw.db")
engine = sqlalchemy.create_engine(conn_string)

# Create a session
session_maker = sqlalchemy.orm.sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

event.listen(session, "before_commit", my_before_commit)

add_order(session)

upd_order(session)

anOrder = models.Order()  # type: models.Order
