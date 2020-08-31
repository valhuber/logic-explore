
class ParentAdjuster:
    """
    Passed to <aggregate>.adjust_parent who will set parent row(s) values
    iff adjustment is required (e.g., summed value changes, where changes, fk changes, etc)
    """

    parent_role = None  # which parent are we dealing with?
    row_logic_state = None  # the child (curr, old values)

    parent_row = None  # values updated by aggregate.adjust_parent()
    old_parent_row = None

    prev_parent_row = None  # child re-parented!
    prev_old_parent_row = None

    def save_altered_parents(self):
        print(str(self))  # more on this later
        # save *only altered* parents (often does nothing)
