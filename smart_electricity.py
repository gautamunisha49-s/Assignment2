
# Q9: Smart Nepal Electricity Meters

meters = {
    "H-101": [1200, 1265, 1340, 1520, 1590],
    "H-102": [880, 910, 945, 975, 1010],
    "H-103": [2300, 2420, 2470, 2530, 2700]
}

slabs = [
    (20, 4),
    (30, 7),
    (50, 9),
    (float("inf"), 11)
]

total_revenue = 0

for house, readings in meters.items():

    # Monthly consumption store garne list
    monthly_units = []

    # Current ra previous reading ko difference nikalne
    for i in range(1, len(readings)):
        consumption = readings[i] - readings[i - 1]
        monthly_units.append(consumption)

    average = sum(monthly_units) / len(monthly_units)

    # Latest month ko consumption
    remaining = monthly_units[-1]

    bill = 0

    # Slab anusar bill calculate garne
    for units, rate in slabs:

        # Current slab ma kati units bill garne
        used = min(remaining, units)

        # Units lai rate sanga multiply garne
        bill += used * rate

        # Billed units ghataune
        remaining -= used

        # Sabai units ko bill bhayepachi stop garne
        if remaining <= 0:
            break

    # Latest bill total revenue ma add garne
    total_revenue += bill

    print(f"{house}: monthly units {monthly_units}, avg {average:.1f}, latest bill Rs {bill}")


# Consumption ma 50% bhanda dherai increase check garne
print("Spikes (>50% jump):")

for house, readings in meters.items():

    # Monthly consumption feri calculate garne
    monthly_units = []

    for i in range(1, len(readings)):
        monthly_units.append(readings[i] - readings[i - 1])

    # Previous ra current month compare garne
    for i in range(1, len(monthly_units)):

        previous = monthly_units[i - 1]
        current = monthly_units[i]

        # Previous month ko 50% bhanda dherai increase bhaye
        if current > previous * 1.5:
            print(f"  {house} month {i + 1}: {previous} -> {current} units")

print("Total latest-month revenue: Rs", total_revenue)
