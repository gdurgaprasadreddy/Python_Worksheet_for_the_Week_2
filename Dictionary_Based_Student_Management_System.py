students = {
    "Durga": {"marks": 66, "grade": "C"},
    "Ravi": {"marks": 93, "grade": "A+"},
    "Madhu": {"marks": 74, "grade": "B"},
    "Vivek": {"marks": 83, "grade": "A"},
    "Nikhil": {"marks": 91, "grade": "A+"}
}
print("Student Details:")

for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])
    print()
highest_student = ""
highest_marks = 0

for name, details in students.items():
    if details["marks"] > highest_marks:
        highest_marks = details["marks"]
        highest_student = name
print("Student with Highest Marks:")
print("Name:", highest_student)
print("Marks:", highest_marks)
print("Grade:", students[highest_student]["grade"])
