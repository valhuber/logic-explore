from logic_engine.rule_bank.rule_bank import RuleBank
from logic_engine.rule_type.derivation import Derivation


class Formula(Derivation):

    def __init__(self, derive: str, calling: str):
        super(Formula, self).__init__(derive)
        self._function = calling
        rb = RuleBank()
        rb.deposit_rule(self)

    def __str__(self):
        return super().__str__() + \
               f'Formula Function: {self._function} '
