from logic_engine.rule_type.derivation import Derivation


class Aggregate(Derivation):

    def __init__(self, derive: str):
        super(Aggregate, self).__init__(derive)

