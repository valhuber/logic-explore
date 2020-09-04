from logic_engine.exec_row_logic.logic_row import LogicRow
from logic_engine.rule_bank import rule_bank_withdraw
from logic_engine.rule_type.formula import Formula


class RowLogicExec:

    def __init__(self, logic_row: LogicRow):
        self.logic_row = logic_row

    def __str__(self) -> str:
        return str(self.logic_row)

    def log(self, msg: str):
        print(msg + ": " + str(self))  # more on this later

    def early_actions(self):
        self.log("early_actions")

    def copy_rules(self):
        self.log("copy_rules")
        copy_rules = rule_bank_withdraw.copy_rules(self.logic_row.name)
        for role_name, copy_rules_for_table in copy_rules.items():
            logic_row = self.logic_row
            if logic_row.ins_upd_dlt == "ins" or logic_row.is_different_parent(role_name):
                parent_logic_row = logic_row.get_parent_logic_row(role_name)
                for each_copy_rule in copy_rules_for_table:
                    each_copy_rule.execute(self.logic_row, parent_logic_row)

    def formula_rules(self):
        self.log("formula_rules")  # TODO (big) execute in dependency order
        formula_rules = rule_bank_withdraw.rules_of_class(self.logic_row.name, Formula)
        for each_formula in formula_rules:
            each_formula.execute(self.logic_row)

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
