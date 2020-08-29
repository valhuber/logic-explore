from builtins import function
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
    def sum_rule(derive: str, as_sum_of: str, where: str = ""):
        """
        Sums designated child data into parent
        Optimized to eliminate / minimize SQLs: Pruning, Adjustment Logic
        """
        pass

    @staticmethod
    def constraint_rule(validate: str, calling: str):
        pass

    @staticmethod
    def formula_rule(derive: str, calling: str):
        pass

    @staticmethod
    def copy_rule(derive: str, from_parent: str):
        pass

""""
class Constraint(Object):
    def __init__(self, row, old_row, logic_context: LogicContext):
        # exec code

class Sum(row: Base, old_row: Base, qual: bool):
    pass
"""