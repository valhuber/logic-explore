from sqlalchemy.orm import session

def my_before_commit(a_session: session):
    print("logic: before commit!")
