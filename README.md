BGU Mart – Supermarket Management System
========================================

BGU Mart is a Python & SQLite-based application designed to efficiently manage supermarket chains.
It tracks employees, suppliers, products, branches, and logs sales and supply activities for accurate inventory management and reporting.

Features
--------

- Database Initialization: Create and populate the database from a configuration file.
- Activity Management: Handle sales and supply deliveries with automatic quantity validation.
- Detailed Reporting:
  - Employee reports: name, salary, branch location, total sales income.
  - Activity reports: date, product description, quantity, seller, and supplier.
- Persistent Storage: All data is stored in a SQLite database bgumart.db.

Modules
-------

| Module         | Description |
|----------------|-------------|
| initiate.py    | Builds a fresh database and inserts initial data from a configuration file. |
| action.py      | Executes sales and supply actions from an action file. |
| printdb.py     | Prints database tables and generates detailed reports. |

Usage
-----

1. Initialize the database:
