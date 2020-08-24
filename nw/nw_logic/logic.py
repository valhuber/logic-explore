from sqlalchemy.orm import session
from sqlalchemy.testing import db

from nw.nw_logic.order_code import OrderCode
from nw.nw_logic.order_detail_code import OrderDetailCode

"""
register by __init__, called by sqlalchemy

forward events to table-specific code, on a per-row basis
"""

def nw_before_commit(a_session: session):
    print("logic: before commit!")
    # for obj in versioned_objects(a_session.dirty):
    for obj in a_session.dirty:
        print("logic: before commit! --> " + str(obj))
        obj_class = obj.__tablename__
        if obj_class == "Order":
            order_code = OrderCode(obj, a_session)
            order_code.order_commit_dirty()
        elif obj_class == "OrderDetail":
            print("Stub")
    print("logic called: before commit!  EXIT")


def nw_before_flush(a_session: session, a_flush_context, an_instances):
    print("nw_before_flush")
    for each_instance in a_session.dirty:
        print("nw_before_flush flushing Dirty! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "Order":
            order_code = OrderCode(each_instance, a_session)
            order_code.order_flush_dirty()
        elif obj_class == "OrderDetail":
            print("Stub")

    for each_instance in a_session.new:
        print("nw_before_flush flushing New! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "OrderDetail":
            order_detail_code = OrderDetailCode(each_instance, a_session)
            order_detail_code.order_detail_flush_new()
        elif obj_class == "Order":
            order_code = OrderCode(each_instance, a_session)
            order_code.order_flush_new()

    print("nw_before_flush  EXIT")



'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''
