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

import logging
import sys

# Initialize Logging

logic_logger = logging.getLogger('logic_logger')  # for users
logic_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logic_logger.addHandler(handler)

engine_logger = logging.getLogger('engine_logger')  # for internals
engine_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
engine_logger.addHandler(handler)


"""
Design Issues:
    * sqlalchemy base vs. mapped objects
    * rows as dict{}, or sqlalchemy.ext.declarative.api.Base.<thing>
        https://stackoverflow.com/questions/553784/can-you-use-a-string-to-instantiate-a-class
        getattr(sa_row, "attrName")
    * do sqlalchemy joins preserve table identity?
        
Design Notes:
    * exec code: https://www.geeksforgeeks.org/eval-in-python/
"""
