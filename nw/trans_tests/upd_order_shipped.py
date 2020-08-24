from datetime import datetime

from sqlalchemy import inspect

import nw.nw_logic.models as models
from nw.nw_logic import session  # opens db, activates logic listener <--


""" toggle Shipped Date, to trigger balance adjustment """
test_order = session.query(models.Order).filter(models.Order.Id == 11011).one()
if test_order.ShippedDate is None or test_order.ShippedDate == "":
    test_order.ShippedDate = str(datetime.now())
    print("shipping: ['' -> " + test_order.ShippedDate + "]")
else:
    test_order.ShippedDate = ""
    print("returning ['xxx' -> " + test_order.ShippedDate + "]")
# ship this unshipped order (dates are like 2014-03-24)
# a_session.query(models.Order).update(test_order)  # Order not iterable
insp = inspect(test_order)
session.commit()
print("\nupd_order, completed\n\n")

