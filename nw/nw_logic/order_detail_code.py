import nw.nw_logic.models as models
from sqlalchemy.orm import session, attributes, object_mapper
from logic_engine.utli import get_old_row, row_to_string, row_prt


def order_detail_flush_new(a_row, a_session: session):
    """
    OrderDetail before_flush, new rows
    compute amount, adjust Order.AmountTotal
    .. which adjusts Customer.balance)
    """
    # no "old" in inserts...  old_row = get_old_row(a_row)
    row_prt(a_row, "\norder_detail_flush_new")
    # nice try.. product = row.Product
    product = a_session.query(models.Product).\
        filter(models.Product.Id == a_row.ProductId).one()
    a_row.UnitPrice = product.UnitPrice
    a_row.Amount = a_row.Quantity * a_row.UnitPrice
    order = a_row.OrderHeader
    order.AmountTotal += a_row.Amount  # hmm.. not triggering Order's before_flush
    row_prt(order, "order_detail_flush_new adjusted")


def order_detail_flush_dirty(a_row, a_session: session):
    # lots ToDo - check qty, fk
    raise Exception("\norder_detail_flush_dirty not implemented")


# happens before flush
def order_detail_commit_dirty(a_row, a_session: session):
    old_row = get_old_row(a_row)
    row_prt(a_row, "\norder_detail_commit_dirty")


def order_detail_modified(object):
    print("order_detail_modified")
