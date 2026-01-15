import sqlite3

from persistence import Repository

repo=Repository()

def print_activities():
    print("Activities")
    query = "SELECT * FROM Activities ORDER BY date ASC;"
    rows = repo.execute_command(query)
    for row in rows:
        print(row)


def print_branches():
    print("Branches")
    query = "SELECT * FROM Branches ORDER BY id ASC;"
    rows = repo.execute_command(query)
    for row in rows:
        print(row)


def print_employees():
    print("Employees")
    query = "SELECT * FROM Employees ORDER BY id ASC;"
    rows = repo.execute_command(query)
    for row in rows:
        print(row)


def print_products():
    print("Products")
    query = "SELECT * FROM Products ORDER BY id ASC;"
    rows = repo.execute_command(query)
    for row in rows:
        print(row)


def print_suppliers():
    print("Suppliers")
    query = "SELECT * FROM Suppliers ORDER BY id ASC;"
    rows = repo.execute_command(query)
    for row in rows:
        print(row)


def print_employee_report():
    print("\nEmployees report")
    query = """
        SELECT e.name, e.salary, b.location, SUM(a.quantity * p.price * -1)
        FROM employees e
        LEFT JOIN branches b ON e.branche = b.id
        LEFT JOIN activities a ON a.activator_id = e.id
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY e.id
        ORDER BY e.name
    """
    rows = repo.execute_command(query)
    for row in rows:
        if row[3] is None:
            print(f"{row[0]} {row[1]} {row[2]}" + " 0")
        else:
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


def print_activity_report():
    print("Activities report")
    activities_report = repo.execute_command("""
        SELECT a.date, p.description, a.quantity, e.name, s.name
        FROM activities a
        LEFT JOIN products p ON a.product_id = p.id
        LEFT JOIN employees e ON a.activator_id = e.id
        LEFT JOIN suppliers s ON a.activator_id = s.id
        ORDER BY a.date
    """)

    for row in activities_report:
        print(row)


def main():
    # Print tables
    print_activities()
    print_branches()
    print_employees()
    print_products()
    print_suppliers()

    # Print reports
    print_employee_report()
    print_activity_report()


if __name__ == '__main__':
    main()
