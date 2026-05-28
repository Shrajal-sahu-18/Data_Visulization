import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
scores = np.random.normal(loc = 70,scale = 10,size = 200)
mean_score = np.mean(scores)
plt.hist(scores,bins = 15)
plt.axvline(mean_score,linestyle = "--",color = "red",label = f" mean = {mean_score:.2f}")
plt.xlabel("scores")
plt.ylabel("frequency")
plt.title("histogrames of scores")
plt.legend()
plt.show()
#assianment1 complete



penguins = sns.load_dataset("penguins")
sns.scatterplot(
    data = penguins,
    x = "flipper_length_mm",
    y = "body_mass_g",
    hue = "species"
)
plt.title("Flipper_length vs Body Mass")
plt.xlabel("Flipper_length(mm)")
plt.ylabel("Body Mass (g)")


tips = sns.load_dataset("tips")
plt.figure(figsize = (8,5))