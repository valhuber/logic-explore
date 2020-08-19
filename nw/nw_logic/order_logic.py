import os
import sys

import sqlalchemy

# import logic_engine.logic
sys_exec = sys.executable
sys_path = str(sys.path)
cwd = os.getcwd()

# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#absolute-vs-relative-import
print("Import INSANITY, cwd:        " + cwd)  # chrisyeh@cs.stanford.edu
# print("Import INSANITY, sys_exec: " + sys_exec)  # its the venv python bin
print("Import INSANITY, sys_path: " + sys_path)

'''Works in pycharm
Import INSANITY, cwd:        /Users/val/python/vsc/logic-explore
Import INSANITY, sys_path: ['/Users/val/python/vsc/logic-explore/nw/nw_logic', ...
'''

'''fails in vsc using config.cwd=${workspaceFolder}, BUT same as pycharm!!
Import INSANITY, cwd:        /Users/val/python/vsc/logic-explore
Import INSANITY, sys_path: ['/Users/val/python/vsc/logic-explore/nw/nw_logic', ...
'''

''' fails as script:
Import INSANITY, cwd:        /Users/val/python/vsc/logic-explore/nw/nw_logic
Import INSANITY, sys_path: ['/Users/val/python/vsc/logic-explore/nw/nw_logic', 
                '/Users/val/.pyenv/versions/3.8.3/lib/python38.zip', 
                '/Users/val/.pyenv/versions/3.8.3/lib/python3.8', 
                '/Users/val/.pyenv/versions/3.8.3/lib/python3.8/lib-dynload', 
                '/Users/val/python/vsc/logic-explore/venv/lib/python3.8/site-packages']
'''

from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
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

# Add a Customer - works
new_cust = models.Customer(Id="$$New Cust1", )
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


