import os

import sqlalchemy
from sqlalchemy import event
from sqlalchemy.testing import db

from nw.nw_logic.models import Order

from nw.nw_logic.logic import nw_before_commit, nw_before_flush
from nw.nw_logic.order_code import order_modified

'''
@event.listens_for(models.Order.ShippedDate, 'modified')
def receive_modified(target, initiator):
    print('Order Modified (Decorator - __init__')
'''

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "nw-app/nw.db")
# e.g. 'sqlite:////Users/val/python/vsc/logic-explore/nw-app/nw.db'
engine = sqlalchemy.create_engine(conn_string, echo=True)

'''
@event.listens_for(Order, 'before_update')
def before_update(mapper, connection, target):
    state = db.inspect(target)
    changes = {}

    for attr in state.attrs:
        hist = attr.load_history()

        if not hist.has_changes():
            continue

        # hist.deleted holds old value
        # hist.added holds new value
        changes[attr.key] = hist.added

    # now changes map keys to new values
    print ("before update")
'''

# Create a session
session_maker = sqlalchemy.orm.sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# target, modifier, function
event.listen(session, "before_commit", nw_before_commit)
event.listen(session, "before_flush", nw_before_flush)

# event.listen(Order.ShippedDate, "set", order_modified)
print("session created, listeners registered")
