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


class OrderDetailCode:
    row: models.OrderDetail
    a_session: session

    _row = None
    _old_row = None

    def __init__(self, a_row, a_session: session):
        print("CTOR order_code.OrderDetailCode")
        self._row = a_row
        self._old_row = None
        self._session = a_session

    def order_detail_flush_new(self):
        row = self._row
        old_row = get_old_row(self._row)
        row_prt(row, "\norder_detail_flush_new")
        # nice try.. product = row.Product
        product = self._session.query(models.Product).\
            filter(models.Product.Id == row.ProductId).one()
        row.UnitPrice = product.UnitPrice
        row.Amount = row.Quantity * row.UnitPrice
        order = row.OrderHeader
        order.AmountTotal += row.Amount  # hmm.. not triggering Order's before_flush
        row_prt(order, "order_detail_flush_new adjusted")

    def order_detail_flush_dirty(self):
        # lots ToDo - check qty, fk
        raise Exception("\norder_detail_flush_dirty not implemented")

    # happens before flush
    def order_detail_commit_dirty(self):
        row = self._row
        old_row = get_old_row(self._row)
        row_prt(row, "\norder_detail_commit_dirty")


def order_detail_modified(object):
    print("order_detail_modified")
