from logic_engine.logic import Logic

"""
    Alternative 1: use named arguments
    see Logic class, eg Logic.sum_rule(derive: str, as_sum_of: str, where: str = ""):

    this is nice to read, and works well with code completion for args
"""


class NwLogic(object):

    def check_balance(row, old_row, logic_context) -> bool:
        return row.balance <= row.creditLimit

    def compute_amount(row, old_row, logic_context):
        return row.UnitPrice <= row.Quantity

    Logic.constraint_rule(validate="Customer", calling='check_balance')
    Logic.sum_rule(derive="Customer.balance", as_sum_of="Order.AmountTotal", where="ShippedData not None")
    Logic.sum_rule(derive="Order.AmountTotal", as_sum_of="OrderDetails.Amount")
    Logic.formula_rule(derive="OrderDetail.Amount", calling="compute_amount")
    Logic.copy_rule(derive="OrderDetail.UnitPrice", from_parent="Product.UnitPrice")


'''
    Alternative 2: decorators
    
    1 class for each Domain class, but unable to inherit?...
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

    In this approach, decorators express the logic
    tho, formulas/constraints require Python code
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

