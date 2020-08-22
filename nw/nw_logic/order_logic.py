from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
import nw.nw_logic.models as models
from sqlalchemy.orm import session


'''
    cannot inherit from models.Order...
    Can't place __table_args__ on an inherited class with no table.
'''


class OrderLogic:
    row: models.Order
    a_session: session

    _row = None
    _old_row = None

    def __init__(self, a_row, a_session: session):
        print("creating order logic object")
        self._row = a_row
        self._old_row = None  # FIXME - how is this handled??
        self._session = a_session

    an_order = models.Order()  # type Order
    an_old_order = models.Order()
    # each rule is a function?

    # @sum_rule Order.AmountTotal = sum(OrderDetails.amount)
    def derive_amount_total(self, row: models.Order, old_row: models.Order,
                      child_row: models.OrderDetail) -> int:
        return logic.Sum(row.OrderDetail, "Amount")

    def insert_code(self):
        print("order_logic.insert")

    def update_code(self):
        print("Order Update Code")
        if ((self._row.ShippedDate is not None or
            self._row.ShippedDate > "")
                and self._row.ShippedDate is None):
            customer = self._row.Customer
            customer.Balance += self._row.AmountTotal
            # do it need attaching?
