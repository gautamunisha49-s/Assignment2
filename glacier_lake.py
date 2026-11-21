
# Q7: Glacier Lake Early Warning

lakes = {
    "Tsho Rolpa": (20.0, 24.0, [17.2, 17.5, 18.3, 19.0, 20.1, 22.0, 24.4, 25.0]),
    "Imja": (15.0, 18.0, [12.0, 12.1, 12.3, 12.2, 12.6, 13.0, 13.1, 13.3]),
    "Thulagi": (30.0, 33.0, [28.0, 28.9, 29.5, 30.2, 30.4, 30.1, 29.8, 29.6])
}

# Lake ko status group garne dictionary
status_groups = {
    "Normal": [],
    "Watch": [],
    "Danger": []
}

for lake, data in lakes.items():

    # Tuple bata warning, danger ra readings nikalne
    warning, danger, readings = data

    # Hour-to-hour water level rise store garne list
    rises = []

    for i in range(1, len(readings)):
        rise = readings[i] - readings[i - 1]
        rises.append(round(rise, 2))

    # Suruma status Normal rakheko
    status = "Normal"
    status_hour = None

    # Enumerate le index ra water level dubai dincha
    for hour, level in enumerate(readings):

        # Danger level cross bhaye Danger
        if level >= danger:
            status = "Danger"
            status_hour = hour
            break

        # Warning level cross bhaye Watch
        elif level >= warning and status == "Normal":
            status = "Watch"
            status_hour = hour

    # Consecutive rapid rises count garne
    rapid_streak = 0
    rapid_rise = False

    for rise in rises:

        if rise > 0.5:
            rapid_streak += 1
        else:
            rapid_streak = 0

        # 3 consecutive rises bhaye rapid rise
        if rapid_streak >= 3:
            rapid_rise = True

    # Maximum water level ra biggest rise
    maximum = max(readings)
    biggest_rise = max(rises)

    # Lake ko status group ma add garne
    status_groups[status].append(lake)

    # Status message prepare garne
    message = status

    if status_hour is not None:
        message += f" (from hour {status_hour})"

    if rapid_rise:
        message += " + RAPID RISE"

    print(f"{lake:<11} max {maximum} m, biggest rise {biggest_rise} m, status {message}")

print(status_groups)

# Danger ma bhayeka lakes ko evacuation message
if status_groups["Danger"]:
    print("EVACUATE downstream of:", ", ".join(status_groups["Danger"]))
