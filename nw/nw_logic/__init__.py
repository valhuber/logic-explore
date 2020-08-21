import os

import sqlalchemy
from sqlalchemy import event

from nw.trans_tests.logic import my_before_commit

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)
basedir = os.path.dirname(basedir)
conn_string = "sqlite:///" + os.path.join(basedir, "nw-app/nw.db")
# e.g. 'sqlite:////Users/val/python/vsc/logic-explore/nw-app/nw.db'
engine = sqlalchemy.create_engine(conn_string)

# Create a session
session_maker = sqlalchemy.orm.sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

event.listen(session, "before_commit", my_before_commit)
