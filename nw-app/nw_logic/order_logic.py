import os
import sys

import sqlalchemy

# import logic_engine.logic

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


'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''

