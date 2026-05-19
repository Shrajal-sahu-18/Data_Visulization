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