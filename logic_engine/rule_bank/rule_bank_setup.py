from datetime import datetime

from sqlalchemy import event

from logic_engine.exec_trans_logic.listeners import before_flush
from logic_engine.rule_bank.rule_bank import RuleBank
from nw.nw_logic import session


def setup(a_session: session = None):
    rules_bank = RuleBank()
    rules_bank._session = a_session
    event.listen(a_session, "before_flush", before_flush)
    rules_bank._tables = {}
    rules_bank._at = datetime.now()
    return
