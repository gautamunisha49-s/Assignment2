
# Q6: Mobile Game Match History

matches = [
    ("W", 10, 1, 5, "Layla"),
    ("W", 3, 2, 4, "Tigreal"),
    ("L", 2, 6, 3, "Layla"),
    ("W", 8, 0, 6, "Gusion"),
    ("W", 5, 2, 9, "Layla"),
    ("W", 1, 3, 12, "Tigreal"),
    ("L", 4, 5, 2, "Gusion"),
    ("W", 7, 2, 8, "Layla")
]

wins = 0
current_streak = 0
longest_streak = 0

# Each hero ko KDA store garne dictionary
hero_kda = {}

# Each hero ko match history check garne
for result, kills, deaths, assists, hero in matches:

    # Win bhaye total wins ra current streak badhaune
    if result == "W":
        wins += 1
        current_streak += 1

        # Longest streak update garne
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        # Loss bhaye winning streak reset garne
        current_streak = 0

    # Death zero bhaye denominator 1 use garne
    if deaths == 0:
        deaths = 1

    kda = (kills + assists) / deaths

    # Hero dictionary ma pahila chaina bhane empty list banaune
    if hero not in hero_kda:
        hero_kda[hero] = []

    # Tyo hero ko KDA list ma add garne
    hero_kda[hero].append(kda)

win_rate = (wins / len(matches)) * 100

print(f"Win rate: {win_rate:.1f}%  Longest win streak: {longest_streak}")

# Each hero ko games ra average KDA calculate garne
for hero, kdas in hero_kda.items():

    games = len(kdas)
    average_kda = sum(kdas) / games

    print(f"{hero:<8} games {games}, avg KDA {average_kda:.2f}")

# Most played hero khojne
most_played = max(hero_kda, key=lambda hero: len(hero_kda[hero]))

print("Most played hero:", most_played)
