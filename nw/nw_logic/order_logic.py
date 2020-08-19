import os

import sqlalchemy

from logic_engine import logic
from typing import NewType
import nw.nw_logic.models as models


class OrderLogic():  # Logic class per table
    '''
        cannot inherit from models.Order...
        Can't place __table_args__ on an inherited class with no table.
    '''
    an_order = models.Order()  # type Order
    an_old_order = models.Order()
    # each rule is a function?

    # @sum_rule Order.amount = sum(OrderDetails.amount where True)
    def derive_amount(self, row: models.Order, old_row: models.Order,
                      child_row: models.OrderDetail) -> int:
        return logic.Sum(row.OrderDetail, "Amount")


    # @Constraint_rule
    def verify_amt(self, Order: models.Order, old_row: models.Order):
        if Order.OrderDate < 0:
            return False
        return True


def print_msg(msg):  # This is the outer enclosing function

    def printer():  # This is the nested function
        print(msg)

    return printer  # returns the nested function

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "Northwind_small.sqlite")
engine = sqlalchemy.create_engine(conn_string)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
'''

try:
    user = session.query(User).one()
except MultipleResultsFound, e:
    print e
    # Deal with it
except NoResultFound, e:
    print e
    # Deal with that as well
'''

# Add a Customer - works
new_cust = models.Customer(Id="$$New Cust", )
session.add(new_cust)
session.commit()

print("\nhello worldDB, completed\n\n")

another = print_msg("Hello")
anOrder = models.Order()  # type: models.Order

'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''


