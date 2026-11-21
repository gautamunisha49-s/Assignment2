
# Q2: Restaurant Orders and Daily Collection


menu = {
    1: ("Momo", 180),
    2: ("Chowmein", 150),
    3: ("Thakali Set", 450),
    4: ("Lassi", 120)
}

# Each string represents euta tableko order
orders = ["1:2,4:2", "3:1,1:1,9:3", "2:3,1:2,4:1"]

# invalid food store garna
invalid_codes = []

# Store euta euta food ko sold quantity 
items_sold = {}

# Store total collection of all tables
daily_collection = 0


# Outer loop
for i, order in enumerate(orders, start=1):

    subtotal = 0

    # split garya like "1:2,4:2" becomes ["1:2", "4:2"]
    items = order.split(",")

    # Inner loop
    for item in items:

        # split garya "1:2" becomes ["1", "2"]
        parts = item.split(":")

        # Convert string values into integers
        code = int(parts[0])
        quantity = int(parts[1])

        if code not in menu:

            invalid_codes.append(code)

            continue

        # Get food name and price from menu
        food_name, price = menu[code]

        amount = price * quantity

        subtotal += amount

        # Count quantity sold for each food
        if food_name not in items_sold:
            items_sold[food_name] = 0

        items_sold[food_name] += quantity

    # Calculate 10% service charge
    service_charge = subtotal * 0.10

    # Calculate 13% VAT on subtotal + service charge
    vat = (subtotal + service_charge) * 0.13

    # Calculate final bill
    final_bill = subtotal + service_charge + vat

    # Add final bill laii daily collection add garnii
    daily_collection += final_bill

    # Print each table's bill
    print(f"Table {i}: subtotal Rs {subtotal}, bill with service + VAT Rs {final_bill:.2f}")


# Find best selling food
best_seller = max(items_sold, key=items_sold.get)

# Print final results
print("Items sold:", items_sold)
print("Best seller:", best_seller, "| Invalid codes:", invalid_codes)
print(f"Day's collection: Rs {daily_collection:.2f}")
