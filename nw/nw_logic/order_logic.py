from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
import nw.nw_logic.models as models


'''
    cannot inherit from models.Order...
    Can't place __table_args__ on an inherited class with no table.
'''


class OrderLogic:
    row: models.Order
    an_old_row: models.Order

    def __init__(self, a_row, an_old_row):
        print("creating order logic object")


    an_order = models.Order()  # type Order
    an_old_order = models.Order()
    # each rule is a function?

    # @sum_rule Order.AmountTotal = sum(OrderDetails.amount)
    def derive_amount_total(self, row: models.Order, old_row: models.Order,
                      child_row: models.OrderDetail) -> int:
        return logic.Sum(row.OrderDetail, "Amount")

    def insert_code(self):
        print("order_logic.insert")

