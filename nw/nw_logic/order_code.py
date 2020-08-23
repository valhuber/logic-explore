from sqlalchemy import event
from sqlalchemy.exc import UnmappedColumnError

from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
import nw.nw_logic.models as models
from sqlalchemy.orm import session, attributes, object_mapper

from logic_engine.utli import get_old_row, row_to_string, row_prt

'''
    cannot inherit from models.Order...
    Can't place __table_args__ on an inherited class with no table.
'''


class OrderCode:
    row: models.Order
    a_session: session

    _row = None
    _old_row = None

    def __init__(self, a_row, a_session: session):
        print("CTOR order_code.OrderCode")
        self._row = a_row
        self._old_row = None  # FIXME - how is this handled??
        self._session = a_session

    # an_order = models.Order()  # type Order
    # an_old_order = models.Order()
    # each rule is a function?

    def insert_code(self):
        print("order_logic.insert")

    # https://docs.sqlalchemy.org/en/13/_modules/examples/versioned_history/history_meta.html
    def order_flush(self):
        print("Order Flush")
        row = self._row
        old_row = get_old_row(self._row)
        row_prt(row, "order_flush")
        if row.ShippedDate != old_row.ShippedDate:
            customer = row.Customer
            delta = row.AmountTotal - old_row.AmountTotal
            customer.Balance += delta
            # does it need attaching?

    # happens before flush
    def order_commit(self):
        print("Order Update Code")
        if ((self._row.ShippedDate is not None or
            self._row.ShippedDate > "")
                and self._row.ShippedDate is None):
            customer = self._row.Customer
            customer.Balance += self._row.AmountTotal
            # do it need attaching?

def order_modified(object):
    print("Order modified")

@event.listens_for(models.Order.ShippedDate, 'modified')
def receive_modified(target, initiator):
    print("Order Modified (Decorator")

'''
    # standard decorator style
    @event.listens_for(SomeClass.some_attribute, 'set')
    def receive_set(target, value, oldvalue, initiator):
        "listen for the 'set' event"

        # ... (event handling logic) ...
    @event.listens_for(SomeClass.some_attribute, 'modified')
    def receive_modified(target, initiator):
        "listen for the 'modified' event"
'''