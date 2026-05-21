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