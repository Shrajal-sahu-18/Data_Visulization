import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y) # line plot
# plt.show()



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
plt.title("Oscar Movies Revenue in each year")
plt.xlabel("years")
plt.ylabel("revenue(in $M)")
# plt.show()

#===========================
#===========================

non_oscar_movies = ["Slumdog millonaire","Avator","Inception","Hugo","Lincoin"]
non_oscar_revenue = [378,2788,829,185,275]
plt.plot(oscar_years,oscar_revenue,color ="#cbc3e3",marker = ">", linestyle = "--", linewidth = 5,label = "oscar_movies")
plt.plot(oscar_years,non_oscar_revenue,"<-g" , label = "Non oscar_movies")
plt.title("oscar movies vs Non_oscar movies revenue")
plt.xlabel("Years")
plt.ylabel("Revenue (In $M)")
plt.legend()
plt.show()


#====================
#====================
with plt.xkcd():
    plt.plot(oscar_years,oscar_revenue,label = "oscar_movies")
    plt.plot(oscar_years,non_oscar_revenue, label = "Non oscar_movies")
    plt.title("oscar movies vs Non_oscar movies revenue")
    plt.xlabel("Years")
    plt.ylabel("Revenue (In $M)")
    plt.legend()
    plt.style.available
    plt.style.use("dark_background")
    plt.style.use("ggplot")
    plt.style.use("default")
    plt.grid()
   

#==================
#==================
oscar_movies = [
    "The Dark Knight",
    "The Hurt locker",
    "The King's Sppech",
    "The Artist",
    "Argo"
]
oscar_years = [2008,2009,2010,2011,2012]
oscar_revenue = [1005,170,427,133,232]
plt.plot(oscar_movies,oscar_revenue)
plt.xlabel("Years")
plt.ylabel("revenue")
plt.title("Movie with revenue")
plt.tight_layout()
plt.savefig("Final_plot.png")


#=============================
#=============================

oscar_movies = [
    "The Dark Knight",
    "The Hurt locker",
    "The King's Sppech",
    "The Artist",
    "Argo"
]
oscar_years = [2008,2009,2010,2011,2012]
oscar_revenue = [1005,170,427,133,232]
plt.bar(oscar_years,oscar_revenue,color = "k")
plt.title("Revenue in Each year")
plt.xlabel("years")
plt.ylabel("revenue")
for i in range(len(oscar_years)):
    plt.text(oscar_years[i],oscar_revenue[i]+7,str(oscar_revenue[i]),ha ="center")
plt.ylim(0,max(oscar_revenue)+100)
plt.xlim(min(oscar_years),max(oscar_years)+5)



oscar_movies = [
    "The Dark Knight",
    "The Hurt locker",
    "The King's Sppech",
    "The Artist",
    "Argo"
]
oscar_revenue = [1005,170,427,133,232]

non_oscar_movies = ["Slumdog millonaire","Avator","Inception","Hugo","Lincoin"]
non_oscar_revenue = [378,2788,829,185,275]

years = [2008,2009,2010,2011,2012]

plt.bar(years,oscar_revenue,label = "oscar_revenue") 
plt.bar(years,non_oscar_revenue,label = " non-oscar_revenue") 
import numpy as np
x = np.arange(len(years))
width = 0.4
plt.bar(x-width/2,oscar_revenue,width,label = "oscar_revenue") # shifting to left 
plt.bar(x+width/2,non_oscar_revenue,width,label = " non-oscar_revenue") # shifting right side
# for 3 bars
# width = 0.25
# plt.bar(x-width,oscar_revenue,width,label = "oscar_revenue")
# plt.bar(x,non_oscar_revenue,width,label = " non-oscar_revenue") 
# plt.bar(x+width,oscar_revenue,width,label = " non-oscar_revenue")
plt.title("oscar movie vs Non oscar movie revenue")
plt.xlabel("years")
plt.ylabel("Revenue (in $m)")
plt.legend()



#horizontal chart
oscar_movies = [
    "The Dark Knight",
    "The Hurt locker",
    "The King's Sppech",
    "The Artist",
    "Argo"
]
# oscar_years = [2008,2009,2010,2011,2012]
oscar_revenue = [1005,170,427,133,232]
plt.barh(oscar_movies,oscar_revenue,label = "Oscar_revenue")
plt.xlabel("revenue")
plt.ylabel("Movie Revenue")



#scatter plots
people = ["Person A", "Person B", "Person C","Person D","Person E"
         ,"Person F", "Person G", "Person H", "Person I", "Person J"]
age = [22,25,30,35,40,45,50,55,60,65]
blood_pressure = [110,115,120,122,125,130,135,123,145,150]