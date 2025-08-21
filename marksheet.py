s_name = input("Enter student name:")
e_no = input("Enter student enrollment number:")

subjects = []
marks = []
total_mark = 0
print("\nEnter names and marks of subjects")
for i in range(5):
    subject = input(f"Enter names of subject{i+1}:")
    mark = float(input(f"enter marks for {subject} (out of 100):"))
    subjects.append(subject)
    marks.append(mark)
    total_mark += mark

percentage = total_mark/5

print("\n=========================STUDENT MARKSHEET==================")
print(f"Name:{s_name}")
print(f"EnrollmentNo:{e_no}")
print("------------------------------------------------------------")
for i in range(5):
    print(f"{subjects[i]:15}:{marks[i]}")
print("---------------------------------------------")
print(f"total mark:{total_mark}/500")
print(f"percentage:{percentage:2f}%")
print("====================================================")
