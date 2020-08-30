from logic_engine.logic_loader.load_logic import LoadLogic
from logic_engine.rule_type.aggregate import Aggregate


class Sum(Aggregate):

    _as_sum_of = ""
    _where = ""

    def __init__(self, derive: str, as_sum_of: str, where: str):
        super(Sum, self).__init__(derive)
        self._as_sum_of = as_sum_of  # could probably super-ize parent accessor
        self._where = where
        ll = LoadLogic("")
        ll.load_rule(self)

    def __str__(self):
        result = super().__str__() + "as Sum(" + self._as_sum_of
        if self._where != "":
            result += " Where " + self._where
        result += ")"
        return result


"""
   f'as Sum({self._as_sum_of},' \
   f'Where: {self._where})'
"""