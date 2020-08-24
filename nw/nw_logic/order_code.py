from sqlalchemy import event

import nw.nw_logic.models as models
from sqlalchemy.orm import session

from logic_engine.utli import get_old_row, row_prt


# https://docs.sqlalchemy.org/en/13/_modules/examples/versioned_history/history_meta.html
def order_flush_dirty(a_row, a_session: session):
    """
    Called from logic.py on before_flush
    E.g., altering an Order ShippedDate (we must adjust Customer balance)
    """
    old_row = get_old_row(a_row)
    row_prt(a_row, "\norder_flush_dirty")

    if a_row.ShippedDate != old_row.ShippedDate:
        is_unshipped = (a_row.ShippedDate is None) or (a_row.ShippedDate == "")
        delta = - a_row.AmountTotal  # assume not changed!!
        if is_unshipped:
            delta = a_row.AmountTotal
        customer = a_row.Customer
        customer.Balance += delta  # attach, update not req'd
        row_prt(customer, "order_flush_dirty adjusted per shipped change")

    if a_row.AmountTotal != old_row.AmountTotal:
        customer = a_row.Customer
        delta = a_row.AmountTotal - old_row.AmountTotal
        customer.Balance += delta  # attach, update not req'd
        row_prt(customer, "order_flush_dirty adjusted per AmountTotal change")


def order_flush_new(a_row, a_session: session):
    """
    Called from logic.py on before_flush
    """
    row = a_row
    row_prt(a_row, "order_flush_new - no logic required")


# happens before flush
def order_commit_dirty(a_row, a_session: session):
    old_row = get_old_row(a_row)
    row_prt(a_row, "order_commit_dirty")


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