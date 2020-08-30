from logic_engine.logic_loader.rule_bank import RuleBank
from logic_engine.rule_type.aggregate import Aggregate


class Sum(Aggregate):

    _as_sum_of = ""
    _where = ""

    def __init__(self, derive: str, as_sum_of: str, where: str):
        super(Sum, self).__init__(derive)
        self._as_sum_of = as_sum_of  # could probably super-ize parent accessor
        self._where = where
        rb = RuleBank("")
        rb.load_rule(self)

    def __str__(self):
        if self._where != "":
            result = super().__str__() + f'Sum({self._as_sum_of} Where {self._where})'
        else:
            result = super().__str__() + f'Sum({self._as_sum_of})'
        return result

