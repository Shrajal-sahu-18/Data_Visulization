import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.get_dataset_names()
tips =sns.load_dataset("tips")
print(type(tips))
print(tips.head())
sns.set_theme(style = "darkgrid")
sns.relplot(
    data = tips,
    x= "total_bill",
    y = "tip",
    hue = "smoker",
    size = "size",
    style = "smoker"
)

x_val =[1,2,3,4,5,6,7,8,9,10]
y_val = [i**2 for i in x_val]
sns.set_theme(style = "ticks")
sns.relplot(
    x= x_val,
    y = y_val,
    kind = "line"
   
)

sns.load_dataset("tips")
sns.scatterplot(
    data=tips,
    x = "total_bill",y = "tip",
    hue = "time"
    
)