from sqlalchemy.orm import session


def before_flush(a_session: session, a_flush_context, an_instances):
    print("logic.logic_exec.listeners>before_flush BEGIN")
    for each_instance in a_session.dirty:
        table_name = each_instance.__tablename__
        print("logic.logic_exec.listeners>before_flush flushing Dirty! "
              + str(table_name) + "]--> " + str(each_instance))

    for each_instance in a_session.new:
        table_name = each_instance.__tablename__
        print("logic.logic_exec.listeners>before_flush flushing New! "
              + str(table_name) + "]--> " + str(each_instance))

    print("logic.logic_exec.listeners>before_flush  END")
