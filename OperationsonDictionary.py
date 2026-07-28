student = {
    "name": "Aarav",
    "grade": 10,
    "city": "Chennai"
}

print("Original Dictionary:", student)

# 1. Access a value
print("Name:", student["name"])

# 2. Access using get()
print("Grade:", student.get("grade"))

# 3. Add a new key-value pair
student["school"] = "ABC Public School"
print("\nAfter Adding:", student)

# 4. Update a value
student["grade"] = 11
print("After Updating Grade:", student)

# 5. Remove a key-value pair using pop()
student.pop("city")
print("After Removing City:", student)

# 6. Display all keys
print("Keys:", student.keys())

# 7. Display all values
print("Values:", student.values())

# 8. Display all key-value pairs
print("Items:", student.items())

# 9. Check if a key exists
print("Is 'name' present?", "name" in student)

# 10. Length of dictionary
print("Total Entries:", len(student))

# 11. Clear the dictionary
student.clear()
print("After Clear:", student)
