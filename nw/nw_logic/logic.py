from sqlalchemy.orm import session
from sqlalchemy.testing import db

from nw.nw_logic.order_code import OrderCode


def nw_before_commit(a_session: session):
    print("logic: before commit!")
    # for obj in versioned_objects(a_session.dirty):
    for obj in a_session.dirty:
        print("logic: before commit! --> " + str(obj))
        obj_class = obj.__tablename__
        if obj_class == "Order":
            order_code = OrderCode(obj, a_session)
            order_code.order_commit()
        elif obj_class == "OrderDetail":
            print("Stub")
    print("logic called: before commit!  EXIT")


def nw_before_flush(a_session, a_flush_context, an_instances):
    print("logic: before flush!")
    for each_instance in a_session.dirty:
        print("logic: flushing! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "Order":
            order_code = OrderCode(each_instance, a_session)
            order_code.order_flush()
        elif obj_class == "OrderDetail":
            print("Stub")

    print("logic called: before commit!  EXIT")



'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''
