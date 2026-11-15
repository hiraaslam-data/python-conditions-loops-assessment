"""
Task 2: Smart Pharmacy Inventory & Sales Management System
Topic: Loop Structures (for, range(), conditions in loops, counters, accumulators)
"""

LOW_STOCK_LIMIT = 10


def get_int(prompt, minimum):
    """Ask for a whole number >= minimum until valid input is given."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Value must be {minimum} or more.")
            continue
        return value


def get_price(prompt):
    """Ask for a price greater than zero until valid input is given."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if value <= 0:
            print("Price must be greater than 0.")
            continue
        return value


def get_medicine_name(prompt):
    """Ask for a non-empty medicine name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Medicine name cannot be empty.")


def main():
    print("=" * 55)
    print("   SMART PHARMACY INVENTORY & SALES MANAGEMENT")
    print("=" * 55)

    # 1. How many medicines to process
    total_medicines = get_int("How many different medicines to process? ", 1)

    # Accumulators and counters
    total_revenue = 0.0        # accumulator: money earned
    restock_count = 0          # counter: medicines needing restock
    successful_sales = 0       # counter: sales that went through
    failed_sales = 0           # counter: sales rejected (not enough stock)
    restock_list = []          # names of medicines to restock

    # 2. Process each medicine with a for loop
    for i in range(1, total_medicines + 1):
        print(f"\n--- Medicine {i} of {total_medicines} ---")

        # 3. Collect details (with validation)
        name = get_medicine_name("Medicine name: ")
        stock = get_int("Available stock: ", 0)
        price = get_price("Price per unit (Rs.): ")
        quantity = get_int("Quantity sold: ", 0)

        # 4. Check stock availability
        if quantity > stock:
            failed_sales += 1
            print(f"Sale rejected: only {stock} unit(s) of {name} in stock.")
            remaining = stock  # nothing was sold
        else:
            # 5. Calculate sales amount
            sale_amount = quantity * price
            total_revenue += sale_amount     # update accumulator
            successful_sales += 1

            # 6. Remaining stock
            remaining = stock - quantity
            print(f"Sale amount     : Rs. {sale_amount:,.2f}")
            print(f"Remaining stock : {remaining}")

        # 7 & 9. Low-stock warning and restock counter
        if remaining < LOW_STOCK_LIMIT:
            print(f"WARNING: Low stock for {name} ({remaining} left)!")
            restock_count += 1
            restock_list.append(name)

    # 10. Final report
    print("\n" + "=" * 55)
    print("                 FINAL SALES REPORT")
    print("=" * 55)
    print(f"Total medicines processed      : {total_medicines}")
    print(f"Successful sales               : {successful_sales}")
    print(f"Rejected sales (low stock)     : {failed_sales}")
    print(f"Total revenue                  : Rs. {total_revenue:,.2f}")
    print(f"Medicines requiring restocking : {restock_count}")
    if restock_list:
        print("Restock list                   : " + ", ".join(restock_list))
    print("=" * 55)


if __name__ == "__main__":
    main()