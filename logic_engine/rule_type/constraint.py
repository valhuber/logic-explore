from logic_engine.rule_bank.rule_bank import RuleBank
from logic_engine.rule_type.rule import Rule


class Constraint(Rule):

    _function = None

    def __init__(self, validate: str, calling):
        super(Constraint, self).__init__(validate)
        # self.table = validate  # setter finds object
        self._function = calling
        ll = RuleBank()
        ll.deposit_rule(self)

    def __str__(self):
        return f'Constraint Function: {str(self._function)} '
