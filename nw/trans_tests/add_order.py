import os
import sys

import sqlalchemy
from sqlalchemy import event
from sqlalchemy.orm import session

# import logic_engine.logic

from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
from typing import NewType
import nw.nw_logic.models as models
from nw.nw_logic import session  # opens db, activates logic listener <--


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
    test_order = a_session.query(models.Order).filter(models.Order.id == 11078).one()
    print("\nupd_order, completed\n\n")


add_order(session)

upd_order(session)

anOrder = models.Order()  # type: models.Order
