roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]

student_directory = dict(zip(roll_numbers, names))

print("Student Directory:", student_directory)
print("Student with Roll No. 3:", student_directory[3])
