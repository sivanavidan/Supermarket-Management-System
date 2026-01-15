from persistence import repo
import sys


def main(args: list[str]):
    inputfilename: str = args[1]

    transactions = []
    with open(inputfilename) as inputfile:
        for line in inputfile:
            # Parse the input line
            splittedline: list[str] = line.strip().split(", ")
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]

            # Store transaction as a tuple
            transactions.append((product_id, quantity, activator_id, date))

    # Sort transactions by date
    transactions.sort(key=lambda x: x[3])

    # Process transactions in sorted order
    for product_id, quantity, activator_id, date in transactions:

            # Fetch product details
            product_query = f"SELECT quantity FROM Products WHERE id = {product_id};"
            product_rows = repo.execute_command(product_query)

            # Proceed only if product exists
            if product_rows:
                available_quantity = product_rows[0][0]

                if quantity > 0:  # Delivery (buy)
                    # Update product quantity
                    update_query = f"""
                        UPDATE Products
                        SET quantity = quantity + {quantity}
                        WHERE id = {product_id};
                    """
                    repo.execute_command(update_query)

                    # Insert activity
                    insert_activity_query = f"""
                        INSERT INTO Activities (product_id, quantity, activator_id, date)
                        VALUES ({product_id}, {quantity}, {activator_id}, '{date}');
                    """
                    repo.execute_command(insert_activity_query)

                elif quantity < 0:  # Sale
                    if available_quantity >= abs(quantity):  # Check sufficient stock
                        # Update product quantity
                        update_query = f"""
                            UPDATE Products
                            SET quantity = quantity + {quantity}
                            WHERE id = {product_id};
                        """
                        repo.execute_command(update_query)

                        # Insert activity
                        insert_activity_query = f"""
                            INSERT INTO Activities (product_id, quantity, activator_id, date)
                            VALUES ({product_id}, {quantity}, {activator_id}, '{date}');
                        """
                        repo.execute_command(insert_activity_query)

                    # Skip the action silently if there's insufficient stock
                    else:
                        continue


if __name__ == '__main__':
    main(sys.argv)
