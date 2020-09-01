class LogicRow:
    """
    state for row logic execution (wraps row, with mold_row, ins_upd_dlt, nest_level, etc)
    """

    def __init__(self, row, old_row, ins_upd_dlt, nest_level):
        self.row = row
        self.old_row = old_row
        self.ins_upd_dlt = ins_upd_dlt
        self.nest_level = nest_level

    def __str__(self):
        result = self.row.__tablename__ + "[]: "  # TODO add [pk]
        cols = self.row.__table__.columns
        is_first = True
        for each_col in cols:
            each_col_name = each_col.name
            if not is_first:
                result += ", "
            is_first = False
            if each_col_name == "Idxx":
                print("Debug Stop here")
            value = getattr(self.row, each_col_name)
            result += each_col_name + ": "
            old_value = value
            if self.old_row is not None:
                old_value = getattr(self.old_row, each_col_name)
            if value != str(old_value):
                result += ' [' + str(old_value) + '-->]'
            if isinstance(value, str):
                result += value
            else:
                result += str(value)
        return result  # str(my_dict)
