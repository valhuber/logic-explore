from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import SchemaItem
from sqlalchemy_utils import get_class_by_table

# from logic_engine.logic import Base


class Rule(object):

    table = None

    def __init__(self, a_table_name: str):
        #  failed -- mapped_class = get_class_by_table(declarative_base(), a_table_name)  # User class
        self.table = a_table_name

    def execute(self, row, old_row, context):
        raise Exception("Not Implemented - Subclass Responsibility")