import matplotlib.pyplot as plt
students = ["Aman","Riya","Kabir","Neha","Raj"]
marks = [78,92,67,88,75]
attendence = [85,95,70,90,80]
#grade distribution
grades = ["A","B","C"]
grade_count = [2,2,1]
#figure 
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.bar(students,marks) #1
plt.title("Student Marks")
plt.xlabel("student name")
plt.ylabel("marks")


# # highest marks annotations
# #==================
# #2
max_marks = max(marks)
max_index = marks.index(max_marks)
plt.annotate("Highest",xy = (students[max_index],max_marks) ,xytext = (students[max_index],max_marks + 5),
             arrowprops = dict(facecolor = "black",shrink = 0.05)
            )



# #bar chart
plt.barh(students,attendence, color = "orange")
plt.title("attendence")
plt.xlabel("attendence %")
plt.ylabel("students")



#=================
# pie chart
plt.pie(grade_count,labels = grades,autopct ="%1.1f%%",startangle = 90)
plt.title("grade disribution")


#line plot
plt.subplot(2,2,4)

plt.plot(students,marks,marker = "o",linestyle = "--")
plt.title("marks trend")
plt.xlabel("students")
plt.ylabel("Marks")
plt.grid()
plt.tight_layout()#layout
plt.show()#show

#assianment - 2
matches = [1,2,3,4,5]
virat = [45,70,30,100,65]
rohit = [35,60,55,80,40]
plt.plot(matches,virat,marker = "o",linestyle = "--",color = "blue",label = "virat")
plt.plot(matches,rohit,marker = "s",linestyle = "-",color = "red",label = "rohit")
plt.title("IPL performance compariasion")
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.grid()
plt.legend()
max_score = max(virat)
max_index = virat.index(max_score)
plt.annotate("Highest Score",xy = (matches[max_index],max_score), xytext = (matches[max_index],max_score+10),arrowprops = dict(facecolor = "black",shrink = 0.05)
)
plt.show()
print("/n project complete")



#mini project
import matplotlib.pyplot as plt
students = ["Aman", "Rahul", "Priya", "Neha", "Riya"]
marks = [85, 72, 90, 78, 88]


plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()



months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1800, 1700, 2100, 2500]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()




categories = ["Food", "Rent", "Travel", "Shopping"]
expenses = [5000, 10000, 3000, 2000]
plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()



import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1000, 1500, 1300, 1800, 2000, 2200]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()



students = ["Aman", "Rahul", "Priya", "Neha", "Riya"]
marks = [85, 72, 90, 78, 88]
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()




expenses = [4000, 8000, 2000, 3000]
labels = ["Food", "Rent", "Travel", "Shopping"]
plt.pie(expenses, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()



import matplotlib.pyplot as plt 
# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 180, 170, 210]

# Create figure
plt.figure(figsize=(8, 5))

# Plot line chart
plt.plot(months, sales, marker='o', color='blue', linewidth=2)

# Add labels and title
plt.title('Monthly Sales Report')
plt.xlabel('Month')
plt.ylabel('Sales')




# Add grid
plt.grid(True)

# Show plot
plt.show()




students = ['A', 'B', 'C', 'D', 'E']
marks = [78, 85, 92, 74, 88]



plt.bar(students, marks, color='skyblue')

plt.title('Student Marks')
plt.xlabel('Students')
plt.ylabel('Marks')



import pandas as pd
import matplotlib.pyplot as plt


# Sample student marks data
data = {
    "Student": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Marks": [85, 92, 78, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print(df)


# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")