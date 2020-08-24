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
        self._old_row = None
        self._session = a_session

    # https://docs.sqlalchemy.org/en/13/_modules/examples/versioned_history/history_meta.html
    def order_flush_dirty(self):
        """
        Called from logic.py on before_flush
        E.g., altering an Order ShippedDate (we must adjust Customer balance)
        """
        row = self._row
        old_row = get_old_row(self._row)
        row_prt(row, "\norder_flush_dirty")
        if row.ShippedDate != old_row.ShippedDate:
            is_unshipped = (row.ShippedDate is None) or (row.ShippedDate == "")
            delta = - row.AmountTotal  # assume not changed!!
            if is_unshipped:
                delta = row.AmountTotal
            customer = row.Customer
            customer.Balance += delta  # attach, update not req'd
            row_prt(customer, "order_flush_dirty adjusted per shipped change")
        if row.AmountTotal != old_row.AmountTotal:
            customer = row.Customer
            delta = row.AmountTotal - old_row.AmountTotal
            customer.Balance += delta  # attach, update not req'd
            row_prt(customer, "order_flush_dirty adjusted per AmountTotal change")


    def order_flush_new(self):
        """
        Called from logic.py on before_flush
        """
        row = self._row
        row_prt(row, "order_flush_new - no logic required")

    # happens before flush
    def order_commit_dirty(self):
        row = self._row
        old_row = get_old_row(self._row)
        row_prt(row, "order_commit_dirty")


# *********************** unused experiments *************************

def order_modified(object):
    print("order_modified - experiment with this (failed, not used)")

@event.listens_for(models.Order.ShippedDate, 'modified')
def receive_modified(target, initiator):
    print("receive_modified - experiment with this (failed, not used)")

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