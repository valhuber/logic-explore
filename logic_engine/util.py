import inspect

from sqlalchemy.exc import UnmappedColumnError
from sqlalchemy.orm import attributes, object_mapper

from nw.nw_logic.models import Base


class ObjectView(object):
    """
    Makes a dict look like a row, enabling old_row.attr
    """

    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        return str(self.__dict__)


def get_old_row(obj) -> ObjectView:
    """
    obtain old_row (during before_flush) from sqlalchemy row

    thanks
        https://docs.sqlalchemy.org/en/13/_modules/examples/versioned_history/history_meta.html
        https://goodcode.io/articles/python-dict-object/
    """
    obj_state = attributes.instance_state(obj)
    old_row = {}
    obj_mapper = object_mapper(obj)
    for each_map in obj_mapper.iterate_to_root():
        # print("each_map: " + str(each_map))  # inheritance tree
        for each_hist_col in obj_mapper.local_table.c:
            # print("each_hist_col: " + str(each_hist_col))
            try:  # prop.key is colName
                prop = obj_mapper.get_property_by_column(each_hist_col)
            except UnmappedColumnError:
                # in the case of single table inheritance, there may be
                # columns on the mapped table intended for the subclass only.
                # the "unmapped" status of the subclass column on the
                # base class is a feature of the declarative module.
                continue

                # expired object attributes and also deferred cols might not
                # be in the dict.  force it to load no matter what by
                # using getattr().
            if prop.key == "ShippedDatexxx":
                print("DEBUG - changed column")  # stop here!
            if prop.key not in obj_state.dict:
                getattr(obj, prop.key)
            a, u, d = attributes.get_history(obj, prop.key)
            # todo prefers .AttributeState.history -- how to code??

            if d:  # changed, and this is the old value
                old_row[prop.key] = d[0]
                obj_changed = True
            elif u:  # unchanged
                old_row[prop.key] = u[0]
            elif a:  # added (old value null)
                # if the attribute had no value.
                old_row[prop.key] = a[0]
                obj_changed = True
    return ObjectView(old_row)


def hydrate_row(a_row: Base) -> Base:
    get_old_row(a_row)
    return a_row


def row2dict(row: Base) -> dict:
    """
    convert sqlalchemy row to dict (e.g, for debug print)
    it's hard to type sqlalchemy
    https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    """
    # result = dict(row)  # fails - not iterable
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)  # FIXME value vs str(getattr(row, column.name))
    return d


def row_to_string(obj) -> str:
    """
    obj can be ObjectVew, or sqlalchemy row
    """
    # return str(obj)

    if type(obj) is ObjectView:
        return str(obj)
    elif hasattr(obj, "__table__"):  # sqlalchemy row
        result = obj.__tablename__ + ": "
        old_row = get_old_row(obj)
        is_first = True
        my_dict = row2dict(obj)
        for each_attr_name in sorted(my_dict.keys()):
            if not is_first:
                result += ", "
            is_first = False
            # print(each_attr_name, end=" ")
            result += each_attr_name
            if each_attr_name == "Idxx":
                print("Debug Stop here")
            value = my_dict[each_attr_name]
            if hasattr(old_row, each_attr_name):
                old_value = getattr(old_row, each_attr_name)
            else:
                old_value = "*"
            if value != str(old_value):
                result += ' [' + str(old_value) + '-->]'
            result += ': ' + str(value)  # FIXME consider optional str
        return result  # str(my_dict)
    else:
        raise Exception("Oops, expected ObjectView or sqlalchemy row")


def row_prt(obj: object, a_msg: str = ""):
    prt = row_to_string(obj)
    print(a_msg + ", " + prt)


def prt(a_msg: str) -> str:
    cur_frame = inspect.currentframe()
    call_frame = inspect.getouterframes(cur_frame, 2)
    return f'{call_frame[1][3]}: {a_msg}'
