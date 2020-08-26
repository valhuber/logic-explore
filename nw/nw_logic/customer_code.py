from sqlalchemy import event

import nw.nw_logic.models as models
from sqlalchemy.orm import session

from logic_engine.utli import get_old_row, row_prt


# https://docs.sqlalchemy.org/en/13/_modules/examples/versioned_history/history_meta.html
def customer_flush_dirty(a_row, a_session: session):
    """
    Called from logic.py on before_flush
    E.g., altering an Order ShippedDate (we must adjust Customer balance)
    """
    old_row = get_old_row(a_row)
    row_prt(a_row, "\ncustomer_flush_dirty")

    if a_row.Balance > a_row.CreditLimit:  # TODO proper Exception type
        raise Exception("\ncustomer_flush credit limit exceeded")


# happens before flush
def customer_commit_dirty(a_row, a_session: session):
    old_row = get_old_row(a_row)
    row_prt(a_row, "order_commit_dirty")

