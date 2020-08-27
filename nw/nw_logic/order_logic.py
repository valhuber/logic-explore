from logic_engine import logic  # see .env file (or pycharm Add Content Roots)
import nw.nw_logic.models as models
from sqlalchemy.orm import session


'''
    cannot inherit from models.Order...
    Can't place __table_args__ on an inherited class with no table.
'''


class OrderLogic:
    """
    This is to explore *declarative* logic.  Not implemented, just imagining.
    In this approach, logic is not (mainly) code, it's spreadsheet-like expressions.
    The engine calls these when (and only when) referenced data changes, pruning other calls.

    They apply to all changes, i.e. cover Use Cases of
    Add Order, Ship Order, UnShip Order, Delete Order
    Change OrderDetail qty/product, ... (~12)

    The sample problem is "check credit" -- executable (someday) design below.
    """

    # @constraint_rule Customer
    def check_credit(self):
        return self.row.Balance <= self.row.CreditLimit

    # @sum_rule Customer.Balance = sum(Order.AmountTotal where ShippedDate is None)
    def derive_balance(self):
        pass  # the logic is in the annotation

    # @sum_rule Order.AmountTotal = sum(OrderDetails.amount)
    def derive_amount_total(self):
        pass

    # @formula_rule OrderDetail
    def derive_amount(self):
        return self.row.Quantity * self.row.ProductPrice

    # @copy_rule OrderDetail.ProductPrice
    def derive_product_price(self):
        pass
