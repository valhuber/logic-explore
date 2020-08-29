"""
Rule Repository
===============

Want a shared copy of rules for engine (e.g, forms/rest server), thread safe.

Alternatives:

    MetaClass
        https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

    Module (import logic_engine)
        Same ref... trying that, simplest
        import logic_engine
        import nw_logic.listeners.py

    sqlalchemy Engine Plug-in

"""

tables = {}  # dict, key is table name, members are lists of rules


def listx():
    print("\n\nRules by table:\n")

