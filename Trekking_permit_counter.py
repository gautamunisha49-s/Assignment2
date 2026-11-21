# Q1: Trekking permit counter
fees = {
    "Everest": {"Nepali": 100, "SAARC": 1500, "foreign": 3000},
    "Annapurna": {"Nepali": 100, "SAARC": 1000, "foreign": 3000},
    "Langtang": {"Nepali": 100, "SAARC": 1500, "foreign": 3000}
}

visitors = [
    ("Aarav", "Nepali", 22, "Everest"),
    ("Emma", "foreign", 34, "Annapurna"),
    ("Rahul", "SAARC", 8, "Langtang"),
    ("John", "foreign", 65, "Everest"),
    ("Mina", "Nepali", 30, "Annapurna"),
    ("Li", "foreign", 28, "Everest")
]
revenue = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
area_count = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
categories = set()


for name, category, age, area in visitors:

    # Visitor ko area ra category anusar fee nikalne
    fee = fees[area][category]

    if age < 10:
        fee = 0
    elif age >= 60:
        fee = fee // 2

    # Revenue ra visitor count update garne
    revenue[area] += fee
    area_count[area] +=1
    categories.add(category)

    print(f"{name:<6} {area:<10} Rs {fee:>7}")

# Sabai bhanda dherai visitor bhayeko area khojna
busiest = max(area_count, key=area_count.get)
total = sum(revenue.values())

print("Revenue by area:", revenue)
print(f"Busiest area: {busiest} ({area_count[busiest]} visitors)")
print("Visitors categories:", sorted(categories))
print("Total revenue: Rs", total)