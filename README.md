# OLD VERSION

Please [go here](https://github.com/valhuber/python-rules).

Explore sqlalchemy, events, and declarative logic with a running example.   Focus:
* db-generated keys
* update logic (specifically multi-level rollups and old value)
using sqlalchemy events
* web app using Flask AppBuilder's Quickstart

## Installation
Use pycharm, and `pip install -f requirements.txt`.

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
* **Add Order (Check Credit) -** enter an order/orderdetails,
and rollup to AmountTotal / Balance to check CreditLimit
* **Ship / Unship an Order (Adjust Balance) -** when an Order's DateShippped
is changed, adjust the Customers balance

#### Adjustments
Rollups provoke an important design choice: store the aggregate,
or sum things on the fly.  There are cases for both:
   - **Sum** - use sql `select sum` queries to add child data as required.
   This eliminates consistency risks with storing redundant data
   (i.e, the aggregate becomes invalid if an application fails to
   adjust it in *all* of the cases).
   
   - **Stored Aggregates** - a good choice when data volumes are large, and / or chain,
   since the application can **adjust** (make a 1 row update) the aggregate based on the
   *delta* of the children.  Imagine, for example, a customer might have
   thousands of Orders, each with thousands of OrderDetails.

This design decision can dominate application coding.  It's nefarious,
since data volumes may not be known whn coding begins.  (Ideally, this can be
a "late binding" decision, like a sql index.)

In this example, we use the **Stored Aggregate** approach, in order
to investigate multi-table update logic chaining, where updates to 1 row
trigger updates to others rows, which further chain to still more rows.
Here, the stored aggregates are `Customer.Balance`, and `Order.AmountTotal`
(a *chained* aggregate).

## Explore
The [by-code](https://github.com/valhuber/logic-explore/wiki/by-code)
and [by-rules](https://github.com/valhuber/logic-explore/wiki/by-code)
approaches are described in the 
[wiki](https://github.com/valhuber/logic-explore/wiki).


## Flask App Builder
You can also run an app (generated by [fab-quick-start](https://github.com/valhuber/fab-quick-start/wiki)), though this is not currently enforcing logic.

```
cd nw-app
export FLASK_APP=app
flask run
```
