from logic_engine.exec_row_logic.parent_adjuster import ParentAdjuster
from logic_engine.rule_type.derivation import Derivation


class Aggregate(Derivation):

    def __init__(self, derive: str):
        super(Aggregate, self).__init__(derive)

    def adjust_parent(self, a_parent_adjustor: ParentAdjuster):
        raise Exception("Not implemented - subclass responsibility")

