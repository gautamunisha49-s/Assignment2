
# Q8: Forest Fire Risk

districts = [
    ("Chitwan", "Bagmati", 36, 18, 25, 40),
    ("Kaski", "Gandaki", 27, 55, 10, 5),
    ("Dang", "Lumbini", 33, 30, 35, 20),
    ("Bardiya", "Lumbini", 38, 15, 32, 35),
    ("Ilam", "Koshi", 24, 70, 8, 3),
    ("Makwanpur", "Bagmati", 31, 40, 18, 12)
]

# Risk levels anusar district group garne
risk_groups = {
    "Low": [],
    "Moderate": [],
    "High": [],
    "Extreme": []
}

# High ra Extreme district bhayeka provinces store garne
alert_provinces = set()

for district, province, temp, humidity, wind, days in districts:

    score = 0

    # Temperature ko points
    if temp > 35:
        score += 3
    elif temp > 30:
        score += 2
    elif temp > 25:
        score += 1

    # Humidity ko points
    if humidity < 20:
        score += 3
    elif humidity < 35:
        score += 2
    elif humidity < 50:
        score += 1

    # Wind speed ko points
    if wind > 30:
        score += 2
    elif wind > 15:
        score += 1

    # Days since rain ko points
    if days > 30:
        score += 3
    elif days > 14:
        score += 2
    elif days > 7:
        score += 1

    # Total score bata risk level decide garne
    if score <= 3:
        risk = "Low"
    elif score <= 6:
        risk = "Moderate"
    elif score <= 8:
        risk = "High"
    else:
        risk = "Extreme"

    # District ra score lai risk group ma add garne
    risk_groups[risk].append((district, score))

    # High wa Extreme bhaye province alert list ma add garne
    if risk == "High" or risk == "Extreme":
        alert_provinces.add(province)

# Risk level anusar results print garne
for risk, records in risk_groups.items():
    print(f"{risk:<8}: {records}")

# Alert provinces print garne
print("Provinces to alert:", sorted(alert_provinces))
