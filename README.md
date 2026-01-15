BGU Mart – Supermarket Management System
========================================

BGU Mart is a Python & SQLite-based application designed to efficiently manage supermarket chains.  
It tracks employees, suppliers, products, branches, and logs sales and supply activities for accurate inventory management and reporting.

The system reads data from **configuration files** to initialize the database and **action files** to perform sales or supply operations.

Features
--------

- Database Initialization: Create and populate the database from a configuration file (e.g., config.txt).  
- Activity Management: Handle sales and supply deliveries with automatic quantity validation.  
- Detailed Reporting:
  - Employee reports: name, salary, branch location, total sales income.  
  - Activity reports: date, product description, quantity, seller, and supplier.  
- Persistent Storage: All data is stored in a SQLite database `bgumart.db`.  
- Safe Operations: Sale actions are ignored if insufficient product quantity exists. The system does not print errors and only performs valid operations.

Modules
-------

| Module         | Description |
|----------------|-------------|
| initiate.py    | Builds a fresh database and inserts initial data from a configuration file. |
| action.py      | Executes sales and supply actions from an action file. |
| printdb.py     | Prints database tables and generates detailed reports. |

Database Schema
---------------

The system uses a SQLite database `bgumart.db` with the following tables:

- employees – Employee details: ID, name, salary, branch.  
- suppliers – Supplier information: ID, name, contact.  
- products – Product inventory: ID, description, price, quantity.  
- branches – Branch info: ID, location, number of employees.  
- activities – Sales and supply logs: product, quantity, activator, date.


