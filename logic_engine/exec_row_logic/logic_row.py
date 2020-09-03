import sqlalchemy
import sqlalchemy_utils
from sqlalchemy.ext.declarative import base
from sqlalchemy.engine.reflection import inspection, Inspector

from logic_engine.rule_bank.rule_bank import RuleBank
from sqlalchemy.ext.declarative import declarative_base


class LogicRow:
    """
    Wraps row, with mold_row, ins_upd_dlt, nest_level, etc
    State for row logic execution
    """

    def __init__(self, row: base, old_row: base, ins_upd_dlt: str, nest_level: int):
        self.row = row
        self.old_row = old_row
        self.ins_upd_dlt = ins_upd_dlt
        self.nest_level = nest_level

        rb = RuleBank()
        self.rb = rb
        self.session = rb._session
        self.engine = rb._engine
        self.some_base = declarative_base()

        self.name = type(self.row).__name__
        self.table_meta = row.metadata.tables[type(self.row).__name__]
        self.inspector = Inspector.from_engine(self.engine)

    def get_class_by_tablename(self, tablename):
        """Return class reference mapped to table.

        :param tablename: String with name of table.
        :return: Class reference or None.
        """
        # https://stackoverflow.com/questions/11668355/sqlalchemy-get-model-from-table-name-this-may-imply-appending-some-function-to
        sqlalchemy_base = self.some_base
        models = sqlalchemy_base._decl_class_registry  # FIXME - it's empty
        for c in models.values():
            if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
                return c

    def get_parent(self, role_name: str):
        # no, table obj, not name
        # sqlalchemy_utils.functions.get_tables(mixed)
        cls = sqlalchemy_utils.functions.get_class_by_table(base, role_name, data=None)

        # https://docs.sqlalchemy.org/en/13/core/reflection.html#fine-grained-reflection-with-inspector
        f_keys = sqlalchemy.engine.reflection.Inspector.get_foreign_keys(self.inspector, self.name)
        role_fkey = None
        for each_fkey in f_keys:
            key_name = each_fkey.get('name')
            if key_name is None:  # FIXME just guessing about fkey.name
                key_name = each_fkey.get('referred_table')
            if key_name == role_name:
                role_fkey = each_fkey
                break
        if role_fkey is None:
            raise Exception("logic_row.get_parent cannot find role " + role_name)
        # post_cust = session.query(models.Customer).filter(models.Customer.Id == "ALFKI").one()
        parent_name = role_name  # FIXME wrong
        parent_class = self.get_class_by_tablename(role_name)
        return self  # FIXME placeholder, implementation required

    def is_different_parent(self, role_name: str) -> bool:
        return False # FIXME placeholder, implementation required

    def __str__(self):
        result = self.row.__tablename__ + "["
        my_meta = self.table_meta
        key_cols = my_meta.primary_key.columns.keys()
        is_first = True
        for each_key_col in key_cols:
            if not is_first:
                result += " | "
            is_first = False
            value = getattr(self.row, each_key_col)
            if isinstance(value, str):
                result += value
            else:
                result += str(value)
        result += "] "
        cols = self.row.__table__.columns
        sorted_cols = sorted(cols, key=lambda col: col.name)
        is_first = True
        for each_col in sorted_cols:
            each_col_name = each_col.name
            if not is_first:
                result += ", "
            is_first = False
            if each_col_name == "Idxx":
                print("Debug Stop here")
            value = getattr(self.row, each_col_name)
            result += each_col_name + ": "
            old_value = value
            if self.old_row is not None:
                old_value = getattr(self.old_row, each_col_name)
            if value != str(old_value):
                result += ' [' + str(old_value) + '-->]'
            if isinstance(value, str):
                result += value
            else:
                result += str(value)
        return result  # str(my_dict)

