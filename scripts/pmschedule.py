def round_robin_schedule(teams):
    num_teams = len(teams)
    num_weeks = num_teams - 1
    schedule = []

    for week in range(num_weeks):
        week_schedule = []
        for i in range(num_teams):
            opponent = (i + week + 1) % num_teams
            if i < opponent:
                week_schedule.append((teams[i], teams[opponent]))
        schedule.append(week_schedule)

    return schedule

# Define the teams
teams = [
    "Any Humble Empire USA",
    "The brown storm",
    "Guess Hul's Back",
    "Lapa",
    "El Jefe",
    "Baron Von Lounge",
    "The Charlotte SteelFins",
    "Just be woke",
    "Nabers in Paris",
    "Ashish 69/420",
    "Team name pending",
    "Ai Bot Team"
]

# Define the first week's schedule
week1_schedule = [
    ("Any Humble Empire USA", "The brown storm"),
    ("Guess Hul's Back", "Lapa"),
    ("El Jefe", "Baron Von Lounge"),
    ("The Charlotte SteelFins", "Just be woke"),
    ("Nabers in Paris", "Ashish 69/420"),
    ("Team name pending", "Ai Bot Team")
]

# Generate the remaining weeks' schedules
schedule = round_robin_schedule(teams)
for week in range(1, len(teams)):
    week_schedule = schedule[week - 1]
    print(f"Week {week+1}:")
    for matchup in week_schedule:
        print(f"  {matchup[0]} vs {matchup[1]}")