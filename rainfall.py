
#Q5: Rainfall Stations and Flood Watch

rain = {
    "Kathmandu": [0, 12.5, 70.2, 118.0, 40.1, 0, 1.2],
    "Pokhara": [35.0, 88.4, 20.3, 95.0, 5.0, 0, 0],
    "Biratnagar": [0, 0, 2.0, 10.5, 66.0, 210.5, 130.0]
}

# Heavy rain bhayeka stations store garne
heavy_stations = set()

# Wettest station ko rainfall store garne
wettest_station = ""
highest_total = 0

# Each station ko rainfall check garne
for station, days in rain.items():

    # Total rainfall calculate garne
    total = sum(days)

    # Rain bhayeko days count garne
    rainy_days = 0

    # Peak rainfall nikalne
    peak = max(days)

    # Peak rainfall kun day ma bhayo
    peak_day = days.index(peak) + 1

    streak = 0
    flood_watch = False

    # Each day ko rainfall check garne
    for amount in days:

        if amount > 0:
            rainy_days += 1

        if amount >= 64.5:
            streak += 1
            heavy_stations.add(station)
        else:
            # Heavy rain ko sequence break bhayo
            streak = 0

        # 2 or more consecutive heavy rain bhaye flood watch
        if streak >= 2:
            flood_watch = True

    # Wettest station update garne
    if total > highest_total:
        highest_total = total
        wettest_station = station

    # Flood status print garne
    if flood_watch:
        status = "FLOOD WATCH"
    else:
        status = "normal"

    print(f"{station:<11} total {total:6.1f} mm, rainy days {rainy_days}, peak {peak} mm on day {peak_day}, {status}")

print("Wettest station:", wettest_station)
print("Stations with heavy rain:", sorted(heavy_stations))
