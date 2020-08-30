from logic_engine.logic_loader.load_logic import LoadLogic
from logic_engine.rule_type.rule import Rule


class Constraint(Rule):

    _function = None

    def __init__(self, validate: str, calling):
        super(Constraint, self).__init__(validate)
        # self.table = validate  # setter finds object
        self._function = calling
        ll = LoadLogic("")
        ll.load_rule(self)

    def __str__(self):
        return f'Constraint for table: {self.table}, function: {str(self._function)} '
