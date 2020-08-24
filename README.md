# logic-explore

Explore sqlalchemy, events, declarative logic.

## Installation
Use pycharm, and pip install from `requirements.txt`.

## Background
The subject database is an adaption of nw,
with a few rollup columns added.
For those not familiar, this is basically
Customers, Orders, OrderDetails and Products.

### DB-generated Keys
Observe the use of db-generated keys in `Order`
and `OrderDetail`.

### Logic Specifications
The logic requirements can be summarized in the
following rule-based specification:
```
Constraint: Customer.Balance <= Customer.CreditLimit

Customer.Balance = sum(OrderList.AmountTotal where ShippedDate is empty)

Order.AmountTotal = sum(OrderDetails.Amount)

OrderDetails.Amount = UnitPrice * Quantity

OrderDetails.UnitPrice = copy(Product.UnitPrice)
```
The specification addresses around a
dozen transactions.  Here we look at:
* **Add Order / Check Credit -** enter an order/orderdetails,
and rollup to AmountTotal / Balance to check credit
* **Ship / Unship an Order -** when an Order's DateShippped
is changed, adjust the Customers balance

## Add Order: Check Credit

Here we focus on placing an
order, and checking credit. The focus here
is on multi-level roll-ups, to compute
the balance and check it against the credit.

Execution begins in `trans_tests/add_order.py`.

The import statements runs in `nw_logic/__init__`,
which opens the database and
registers the listener `nw_logic/logic.py`.

It forwards events`before_flush`, , mainly  to `nw_logic/order_details_code.py` and
`nw_logic/order_code.py`.

## Ship / Unship an Order: Adjust Balance

The focus here is on **old values** - we need
to see what the DataShipped *was*, and
what it is changed *to*:
* If it changed from empty to shipped, we need to decrease the balance.
* If it changed from shipped to empty, we decrease the balance.

Flow is as described above, reaching `nw_logic/order_logic.py`
Note the call to `logic_engine/util.get_old_row`.
