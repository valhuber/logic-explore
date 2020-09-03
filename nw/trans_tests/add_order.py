import sqlalchemy_utils

import nw.nw_logic.models as models
from logic_engine.util import row_prt
from nw.nw_logic import session  # opens db, activates logic listener <--

cls = sqlalchemy_utils.functions.get_class_by_table(models.Base, "Product", data=None)

# Add Order - works
pre_cust = session.query(models.Customer).filter(models.Customer.Id == "ALFKI").one()
session.expunge(pre_cust)

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

post_cust = session.query(models.Customer).filter(models.Customer.Id == "ALFKI").one()

print("\nadd_order, update completed\n\n")
row_prt(new_order, "\nnew Order Result")  # $18 + $38 = $56
if new_order.AmountTotal != 56:
    print ("==> ERROR - unexpected AmountTotal: " + str(new_order.AmountTotal) +
           "... expected 56")
row_prt(new_item1, "\nnew Order Detail 1 Result")  # 1 Chai  @ $18
row_prt(new_item2, "\nnew Order Detail 2 Result")  # 2 Chang @ $19 = $38

if post_cust.Balance == pre_cust.Balance + 56:
    row_prt(post_cust, "\nCorrect adjusted Customer Result")
    assert True
else:
    row_prt(post_cust, "\nERROR - incorrect adjusted Customer Result")
    print("\n--> probable cause: Order customer update not written")
    row_prt(pre_cust, "\npre_cust")
    assert False

print("\nadd_order, ran to completion\n\n")


