from logic_engine import engine_logger
from logic_engine.utli import prt
from logic_engine.rule_type.rule import Rule
from datetime import datetime

# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RuleBank(object):
    __metaclass__ = Singleton
    """
    scans for rules, creates the logic_repository
    """

    _url = ""
    _tables = {}  # key = tbl_name, value = list of rules
    _at = datetime.now()

    def __init__(self, url: str = ""):
        if self._url != "":  # FIXME is this right?
            _url = url
            _tables = {}
            _at = datetime.now()

    def load_rule(self, a_rule: Rule):
        prt("begin")
        if a_rule.table not in self._tables:
            self._tables[a_rule.table] = []
        self._tables[a_rule.table].append(a_rule)

    def __str__(self):
        result = f"Rule Bank (loaded {self._at})"
        for each_key in self._tables:
            result += f"\nTable[{each_key}] rules:"
            for each_rule in self._tables[each_key]:
                result += f'\n  {str(each_rule)}'
        return result



