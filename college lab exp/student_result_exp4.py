subjects = ["Python", "DSA", "OOPS", "DBMS", "Statistics"]

marks = []
total = 0

# Taking input for each subject
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)
    total += mark

# Calculating average
average = total / len(subjects)

# Checking pass/fail
result = "Pass"
for mark in marks:
    if mark < 40:
        result = "Fail"
        break

# Assigning grade
if result == "Fail":
    grade = "F"
elif average >= 90:
    grade = "O"
elif average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"

# Output
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Result:", result)
print("Grade:", grade)
