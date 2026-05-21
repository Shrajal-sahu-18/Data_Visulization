#            ----IPL----

#            ----TEAM RUNS----Bar Chart----

import matplotlib.pyplot as plt

teams = ["RCB", "CSK", "MI", "KKR", "SRH"]
runs = [210, 185, 200, 176, 195]

plt.figure(figsize=(8,5))

bars = plt.bar(teams, runs)

for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y + 1, y, ha='center')

plt.title("IPL Team Runs")
plt.xlabel("Teams")
plt.ylabel("Runs")
plt.grid(axis='y')

plt.show()



#                ----player Runs----Line Plot----

import matplotlib.pyplot as plt

matches = [1,2,3,4,5]
virat_runs = [45, 72, 10, 88, 56]

plt.figure(figsize=(8,5))

plt.plot(matches, virat_runs, marker='o', linestyle='--', label="Virat Kohli")

plt.title("Virat Kohli Match Runs")
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.legend()
plt.grid()

plt.show()


#              ----Wickets----Pie Chart----

import matplotlib.pyplot as plt

bowlers = ["Bumrah", "Shami", "Rashid", "Siraj"]
wickets = [18, 15, 12, 10]

explode = [0.1, 0, 0, 0]

plt.figure(figsize=(7,7))

plt.pie(
    wickets,
    labels=bowlers,
    autopct='%1.1f%%',
    explode=explode
)

plt.title("IPL Wickets Distribution")

plt.show()


#            ----Two player Comparison----

import matplotlib.pyplot as plt

matches = [1,2,3,4,5]

virat = [45,72,10,88,56]
rohit = [30,80,40,60,70]

plt.figure(figsize=(8,5))

plt.plot(matches, virat, marker='o', label="Virat Kohli")
plt.plot(matches, rohit, marker='s', label="Rohit Sharma")

plt.title("Virat vs Rohit Runs")
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.legend()
plt.grid()

plt.show()


#               ----Strike Rate Scatter Plot----


import matplotlib.pyplot as plt

players = ["A","B","C","D","E"]

strike_rate = [120,145,160,130,155]
runs = [300,450,500,350,480]

plt.figure(figsize=(8,5))

plt.scatter(strike_rate, runs, s=200)

for i in range(len(players)):
    plt.text(strike_rate[i], runs[i], players[i])

plt.title("Strike Rate vs Runs")
plt.xlabel("Strike Rate")
plt.ylabel("Runs")

plt.grid()

plt.show()


#          ----Match - Wise Team Scoare ----


import matplotlib.pyplot as plt

matches = [1,2,3,4,5]
rcb_scores = [180,210,175,220,190]

avg_score = sum(rcb_scores)/len(rcb_scores)

plt.figure(figsize=(8,5))

plt.plot(matches, rcb_scores, marker='o')

plt.fill_between(matches, rcb_scores, alpha=0.3)

highest = max(rcb_scores)
highest_match = matches[rcb_scores.index(highest)]

plt.scatter(highest_match, highest, s=200)

plt.axhline(avg_score, linestyle='--', label=f'Average = {avg_score:.1f}')

plt.title("RCB Match Scores")
plt.xlabel("Matches")
plt.ylabel("Scores")
plt.legend()
plt.grid()

plt.show()