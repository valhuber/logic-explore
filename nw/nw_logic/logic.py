from sqlalchemy.orm import session

from nw.nw_logic.order_code import order_commit_dirty, order_flush_dirty, order_flush_new
from nw.nw_logic.order_detail_code import order_detail_flush_new

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
            order_commit_dirty(obj, a_session)
        elif obj_class == "OrderDetail":
            print("Stub")
    print("logic called: before commit!  EXIT")


def nw_before_flush(a_session: session, a_flush_context, an_instances):
    print("nw_before_flush")
    for each_instance in a_session.dirty:
        print("nw_before_flush flushing Dirty! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "Order":
            order_flush_dirty(each_instance, a_session)
        elif obj_class == "OrderDetail":
            print("Stub")

    for each_instance in a_session.new:
        print("nw_before_flush flushing New! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "OrderDetail":
            order_detail_flush_new(each_instance, a_session)
        elif obj_class == "Order":
            order_flush_new(each_instance, a_session)

    print("nw_before_flush  EXIT")
