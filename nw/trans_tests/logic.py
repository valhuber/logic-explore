from sqlalchemy.orm import session

def my_before_commit(a_session: session):
    print("logic: before commit!")
    # for obj in versioned_objects(a_session.dirty):
    for obj in a_session.dirty:
        print("logic: before commit! --> " + str(obj))
    print("logic: before commit!  EXIT")



'''
# each rule is an object?
    No, that seems to focus on sys internals, not user view
    More natural is a set of functions - Reactive Functional Logic (vs Reactive Programming)
check_amount = logic.Constraint(row=an_order: Order,
                                old_row=an_old_row: Order,
                                logic_context=a_context: logic.LogicContext)
'''
