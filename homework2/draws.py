import random

class Team:
    def __init__(self, name, country, group):
        self.name = name
        self.country = country
        self.group = group

    def __repr__(self):
        return f"{self.name} ({self.country})"    

teams = [
    Team("PSG", "France", 2),
    Team("Liverpool", "England", 1),
    Team("Inter", "Italy", 1),
    Team("Manchester City", "England", 1),
    Team("Leipzig", "Germany", 2),
    Team("Eintracht Frankfurt", "Germany", 2),
    Team("Napoli", "Italy", 1),
    Team("Porto", "Portugal", 2),
    Team("Club Brugge", "Belgium", 2),
    Team("Benfica", "Portugal", 1),
    Team("Tottenham", "England", 2),
    Team("Milan", "Italy", 1),
    Team("Bayern", "Germany", 1),
    Team("Real Madrid", "Spain", 2),
    Team("Chelsea", "England", 2),
    Team("Dortmund", "Germany", 1),
]

def draw_matches(all_teams):
    winners = [t for t in all_teams if t.group == 1]
    runners_up = [t for t in all_teams if t.group == 2]

    random.shuffle(winners)
    random.shuffle(runners_up)

    matches = []
    possible = True

    temp_runners = list(runners_up)

    for winner in winners:
        valid_opponents = []
        for runner in temp_runners:
            if winner.country == runner.country:
                continue
            if(winner.country == "Ukraine" and runner.counry == "Russia") or \
              (winner.country == "Russia" and runner.counry == "Ukaine"):
                continue
            valid_opponents.append(runner)
        if not valid_opponents:
            possible = False
            break

        opponent = random.choice(valid_opponents)
        matches.append((winner, opponent))
        temp_runners.remove(opponent)
    if possible:
        return matches

result = draw_matches(teams)
for i, match in enumerate(result, 1):
    print(f"Match {i}: {match[0]} vs {match[1]}")