students = ["Durga", "Ravi", "Vivek", "Bhargav", "Arif"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

with open("students.txt", "r") as file:
    content = file.read()

print("Student Names:")
print(content)
student_list = content.splitlines()
print("Total Number of Students:", len(student_list))
