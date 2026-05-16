import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y) # line plot
plt.show()



# Real data
#ocsar winning movies
oscar_movies = [
    "The Dark Knight",
    "The Hurt locker",
    "The King's Sppech",
    "The Artist",
    "Argo"
]
oscar_years = [2008,2009,2010,2011,2012]
oscar_revenue = [1005,170,427,133,232] #  In $M
#plot
plt.plot(oscar_years,oscar_revenue)