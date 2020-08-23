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
        old_row = get_old_row(self._row)
        row_prt(self._row, "row")
        row_prt(old_row, "old_row")
        obj = self._row
        obj_state = attributes.instance_state(obj)
        old_row = {}
        obj_mapper = object_mapper(obj)
        for each_map in obj_mapper.iterate_to_root():
            print("each_map: " + str(each_map))  # inheritance tree
            for each_hist_col in obj_mapper.local_table.c:
                print("each_hist_col: " + str(each_hist_col))
                try:  # prop.key is colName
                    prop = obj_mapper.get_property_by_column(each_hist_col)
                except UnmappedColumnError:
                    # in the case of single table inheritance, there may be
                    # columns on the mapped table intended for the subclass only.
                    # the "unmapped" status of the subclass column on the
                    # base class is a feature of the declarative module.
                    continue

                    # expired object attributes and also deferred cols might not
                    # be in the dict.  force it to load no matter what by
                    # using getattr().
                if prop.key == "ShippedDate":
                    print("DEBUG - changed column")  # stop here!
                if prop.key not in obj_state.dict:
                    getattr(obj, prop.key)
                a, u, d = attributes.get_history(obj, prop.key)
                # todo prefers .AttributeState.history -- how to code??

                if d:  # changed, and this is the old value
                    old_row[prop.key] = d[0]
                    obj_changed = True
                elif u:  # unchanged
                    old_row[prop.key] = u[0]
                elif a:  # added (old value null)
                    # if the attribute had no value.
                    old_row[prop.key] = a[0]
                    obj_changed = True
        if self._row.ShippedDate != old_row.ShippedDate:
            customer = self._row.Customer
            delta = self._row.AmountTotal - old_row.AmountTotal
            customer.Balance += delta
            # do it need attaching?

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