from typing import NewType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LogicContext:
    row = None
    old_row = None
    insert_update_delete = ""
    metadata = None
    nest_level = 0


class Logic:
    @staticmethod
    def sum(child_row: Base):
        return 0


""""
class Constraint(Object):
    def __init__(self, row, old_row, logic_context: LogicContext):
        # exec code

class Sum(row: Base, old_row: Base, qual: bool):
    pass
"""