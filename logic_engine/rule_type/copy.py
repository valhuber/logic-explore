from logic_engine.rule_bank.rule_bank import RuleBank
from logic_engine.rule_type.derivation import Derivation


class Copy(Derivation):

    def __init__(self, derive: str, from_parent: str):
        super(Copy, self).__init__(derive)
        names = from_parent.split('.')
        self._from_table = names[0]
        self._from_column = names[1]
        rb = RuleBank()
        rb.deposit_rule(self)

    def __str__(self):
        return super().__str__() + \
               f'Copy({self._from_table}.{self._from_column})'
