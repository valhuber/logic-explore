# logic-explore

Explore sqlalchemy, events, declarative logic.

##Installation
Use pycharm, and pip install from `requirements.txt`.


##Check Credit

Here we focus on placing an
order, and checking credit.  Observe the use of db-generated keys in `Order`
and `OrderDetail` in this adaption of the `nw`
database.

Execution begins in `trans_tests/add_order.py`.

The import statements runs in `nw_logic/__init__`,
which opens the database and
registers the listener `nw_logic/logic.py`.

It forwards events to `nw_logic/order_code.py` and
`nw_logic/order_code.py`.
