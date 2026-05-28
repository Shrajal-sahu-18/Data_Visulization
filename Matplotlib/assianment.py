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