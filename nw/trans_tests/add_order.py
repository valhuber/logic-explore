from datetime import datetime

from sqlalchemy import inspect

import nw.nw_logic.models as models
from nw.nw_logic import session  # opens db, activates logic listener <--


# Add Order - works
new_order = models.Order(AmountTotal=0, CustomerId="ALFKI", ShipCity="Richmond",
                         EmployeeId=6, Freight=1)
session.add(new_order)

# OrderDetails - https://docs.sqlalchemy.org/en/13/orm/backref.html
new_item1 = models.OrderDetail(ProductId=1, Amount=0,
                               Quantity=1, UnitPrice=18,
                               Discount=0)
new_order.OrderDetailList.append(new_item1)
new_item2 = models.OrderDetail(ProductId=2, Amount=0,
                               Quantity=2, UnitPrice=18,
                               Discount=0)
new_order.OrderDetailList.append(new_item2)
session.commit()
print("\nadd_order, completed\n\n")

