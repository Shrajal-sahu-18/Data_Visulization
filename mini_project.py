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