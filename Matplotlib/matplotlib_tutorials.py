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
plt.scatter(age,blood_pressure,color = "red", s = blood_pressure,marker = ">",alpha = 0.6)
plt.scatter(age,blood_pressure,cmap = "OrRd",c = blood_pressure)
plt.title("People with Blood pressure Rate")
plt.xlabel("age")
plt.ylabel("Blood pressure")
plt.grid()
plt.colorbar(label = "bp")
for i in range(len(people)):
    plt.annotate(people[i],xy = (age[i],blood_pressure[i]),xytext = (age[i]+1,blood_pressure[i]+6))
plt.xlim(min(age),max(age)+10)
plt.ylim(min(blood_pressure),max(blood_pressure)+5)



cities = ["city A","city B","city C","city D","city E"]
# winner: tempretrature (°c) vs humidity
winter_temp = [5,2,10,0,7]
winter_humidity = [80,75,65,85,70]

# summer temprature(°c) vs humidity (%)
summer_temp = [25,30,28,35,27]
summer_humidity = [60,50,55,45,65]
plt.scatter(winter_temp,winter_humidity,label = "winter",)
plt.scatter(summer_temp,summer_humidity,label = "summer")
plt.title("summer vs winter Data")
plt.xlabel("temprature (°c)")
plt.ylabel("humidity in %")
plt.legend()



expenses = ["salary","Rent","Marketing","R&D","Miscellaneous"]
amounts = [500,150,120,100,50]
explode = [0,0,0,0.1,0]# plt.style.use("default")
# colors = ["red","pink","blue","black","yellow"]
plt.style.use("default")
plt.pie(amounts,labels = expenses,autopct ="%1.1f%%",wedgeprops ={ "edgecolor":"black","linewidth":1,"linestyle" :"--"},explode = explode,startangle = 180.,shadow =True)


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
score = np.random.normal(70,10,100)
bins = [0,30,50,70,90,100]
plt.hist(score,color = "blue",edgecolor = "black",bins = bins)
#multiple datasets
legit_transaction = [2.99,5.49,8.99,12.50,14.99,19.99,23.45,29.99,34.99,39.50,45.00,49.99,55.25,60.00,75.99,89.99,120.50,150.00,199.99,249.99,300.75,450.00,600.00,850.00,1200.00]
fraud_transactions = [50,100,150,200,300,500,750,1000,1200,1500,1500,2000,2500,3000,3000]
#transaction amount distribution - legit vs fraud
plt.hist(legit_transaction,color = "green",edgecolor ="black",bins = 10,label ="legit",alpha = 0.5)
plt.hist(fraud_transactions,color = "red",edgecolor ="black",bins = 10,label ="fraud",alpha = 0.5)
plt.axvline(
    x = 33,
    linestyle = "--",
    linewidth = "2",
    color = "red",
    label = "passing marks (33)"
)
plt.title("Transaction amount Distribution - Legit vs Fraud")
plt.xlabel("Amount in $")
plt.ylabel("frequency")
plt.legend()
#box plots
data = [7,8,5,6,9,4,10,12,15]
plt.boxplot(data)
plt.grid(True)
#multiple dataset
group1 = np.random.normal(50,10,100)
group2 = np.random.normal(60,10,100)

plt.boxplot([group1,group2],tick_labels = ["gropu1","group2"],vert = False,showmeans = True,whis= 1.5)
plt.grid(True)
#stack plot 
days = ["mon","tue","wed","thu","fri","sat","sun"]
direct = [50,60,70,80,90,100,110]
organic = [30,40,50,55,60,70,80]
social = [20,25,30,35,40,50,60]
plt.stackplot(days,direct,organic,social,labels = ["Direct","Organic","Social"])
plt.legend()
#subplot
x = [1,2,3,4,5,6,7,8,9,10]
y1 = [np.sqrt(i) for i in x] # sqare root 
y2 = [ i*2 for  i in x] #double
y3 = [i**2 for i in x] # sqare
y4 = [i**3 for i in x] #quebe
plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title("plot1 - sqare root")

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title("plot2 - Double")


plt.subplot(2,2,3)
plt.plot(x,y3)
plt.title("plot3 - Sqare")

plt.subplot(2,2,4)
plt.plot(x,y4)
plt.title("plot1 - Quebe")


fig,ax = plt.subplots(2,2,figsize = (7,7))
ax[0][0].plot(x,y1)
ax[0][0].set_title("Plot1 - sqare root")
ax[0][0].set_xlabel("X axis value")
ax[0][0].set_ylabel("y axis value")

ax[0][1].plot(x,y2)
ax[0][1].set_title("Plot2 -Double")

ax[1][0].plot(x,y3)
ax[1][0].set_title("Plot3 - Sqare")

ax[1][1].plot(x,y4)
ax[1][1].set_title("Plot4 - Quebe")
fig.tight_layout()
fig.suptitle("Multiple Plots")


#Task
days = ["mon","tue","wed","thu","fri"]
cities = ["new york","london","delhi","tokyo"]

temprature = [
    [22,23,21,24,25],#New york
    [18,19,17,20,21],#London
    [30,32,31,33,34],#Delhi
    [25,26,24,27,28]#Tokyo
]
fig,axes = plt.subplots(2,2)
axes = axes.flatten()
for i,ax in enumerate(axes):
    ax.plot(days,temprature[i],marker = "o")
    ax.set_title(cities[i])
    ax.grid(True)