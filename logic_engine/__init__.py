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

# Initialize Logging FIXME does not work (see RuleBank)
logic_logger = logging.getLogger('logic_logger')  # for users
logic_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logic_logger.addHandler(handler)

engine_logger = logging.getLogger('engine_logger')  # internals
logic_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
engine_logger.addHandler(handler)

