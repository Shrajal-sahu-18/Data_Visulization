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