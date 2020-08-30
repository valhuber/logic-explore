from logic_engine.logic_loader.load_logic import LoadLogic
from logic_engine.rule_type.derivation import Derivation


class Formula(Derivation):

    def __init__(self, derive: str, calling: str):
        super(Formula, self).__init__(derive)
        self._function = calling
        ll = LoadLogic("")
        ll.load_rule(self)

    def __str__(self):
        return super().__str__() + \
               f'as Formula, calling: {self._function} '
