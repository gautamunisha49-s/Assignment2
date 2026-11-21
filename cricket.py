
#Q3: Cricket Ball by Ball Scorecard

# Sabai ball ko record euta string ma cha
balls = "1 4 . W 6 wd 2 1 . 4 nb 1 . . W 6 1 lb2"

# String lai space ko basis ma list ma convert garne
ball_list = balls.split()

# Suruma sabai counters zero rakheko
score = 0
wickets = 0
legal_balls = 0
extras = 0
fours = 0
sixes = 0
dot_balls = 0

# Each ball lai one by one check garne
for ball in ball_list:

    # Wide: 1 extra run, legal ball hoina
    if ball == "wd":
        score += 1
        extras += 1
        continue

    # No-ball: 1 extra run, legal ball hoina
    if ball == "nb":
        score += 1
        extras += 1
        continue

    # Leg-byes: 2 extras, tara legal ball ho
    if ball == "lb2":
        score += 2
        extras += 2
        legal_balls += 1
        continue

    # Wicket bhaye wicket count badhaune
    if ball == "W":
        wickets += 1
        legal_balls += 1
        continue

    # Dot ball bhaye dot ball count badhaune
    if ball == ".":
        dot_balls += 1
        legal_balls += 1
        continue

    # Baki numeric ball lai integer ma convert garne
    runs = int(ball)

    # Batsman le banayeko run total score ma add garne
    score += runs

    # Four ra six count garne
    if runs == 4:
        fours += 1
    elif runs == 6:
        sixes += 1

    # Numeric delivery legal ball ho
    legal_balls += 1

# Legal balls bata overs ra remaining balls nikalne
overs = legal_balls // 6
remaining_balls = legal_balls % 6

# Run rate = total runs / overs bowled
run_rate = score / (legal_balls / 6)

# Boundary runs ko percentage nikalne
boundary_runs = (fours * 4) + (sixes * 6)
boundary_percentage = (boundary_runs / score) * 100

print(f"Score: {score}/{wickets} in {overs}.{remaining_balls} overs")
print(f"Extras {extras}, Fours {fours}, Sixes {sixes}, Dot balls {dot_balls}")
print(f"Run rate {run_rate:.2f}, Boundary runs {boundary_runs} ({boundary_percentage:.1f}% of total)")
