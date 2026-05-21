#            ----IPL----

#            ----TEAM RUNS----

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