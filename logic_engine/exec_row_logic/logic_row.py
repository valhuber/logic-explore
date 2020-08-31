class LogicRow:
    """
    state for row logic execution (wraps row, with mold_row, ins_upd_dlt, nest_level, etc)
    """

    def __init__(self, a_row, an_old_row, an_ins_upd_dlt, a_nest_level):
        self.row = a_row
        self.old_row = an_old_row
        self.ins_upd_dlt = an_ins_upd_dlt
        self.nest_level = a_nest_level
