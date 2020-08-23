from datetime import datetime

from sqlalchemy import inspect

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
    """ toggle Shipped Date, to trigger balance adjustment """
    test_order = a_session.query(models.Order).filter(models.Order.Id == 11011).one()
    if test_order.ShippedDate is None or test_order.ShippedDate == "":
        test_order.ShippedDate = str(datetime.now())
        print("shipping: ['' -> " + test_order.ShippedDate + "]")
    else:
        test_order.ShippedDate = ""
        print("returning ['xxx' -> " + test_order.ShippedDate + "]")
    # ship this unshipped order (dates are like 2014-03-24)
    # a_session.query(models.Order).update(test_order)  # Order not iterable
    insp = inspect(test_order)
    a_session.commit()
    print("\nupd_order, completed\n\n")


upd_order(session)
