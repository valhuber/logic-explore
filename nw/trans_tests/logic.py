from sqlalchemy.orm import session

def my_before_commit(a_session: session):
    print("logic: before commit!")



'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''
