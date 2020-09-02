from logic_engine.exec_row_logic.logic_row import LogicRow
from logic_engine.rule_bank import rule_bank_withdraw


class RowLogicExec:

    def __init__(self, logic_row: LogicRow):
        self.row_logic_state = logic_row

    def __str__(self) -> str:
        return str(self.row_logic_state)

    def log(self, msg: str):
        print(msg + ": " + str(self))  # more on this later

    def early_actions(self):
        self.log("early_actions")

    def copy_rules(self):
        self.log("copy_rules")
        copy_rules = rule_bank_withdraw.copy_rules("OrderDetail")

    def formula_rules(self):
        self.log("formula_rules")

    def early_actions(self):
        self.log("early_actions")

    def adjust_parent_aggregates(self):
        self.log("adjust_parent_aggregates")
        """
            for each_parent_role
                parent_adjuster = ParentRoleAdjuster(self, each_parent_role)  # NB - 1 parent save for N sums/counts
                for each_aggregate in each_parent_role
                    each_aggregate.adjust_parent(adjuster)  # adjusts each_parent iff req'd
                parent_adjuster.save_altered_parents()
        """

    def update(self):
        self.early_actions()
        self.copy_rules()
        self.formula_rules()
        self.adjust_parent_aggregates()

    def insert(self):
        self.early_actions()
        self.copy_rules()
        self.formula_rules()
        self.adjust_parent_aggregates()
