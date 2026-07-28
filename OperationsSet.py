fruits = {"apple", "banana", "mango", "orange"}

print("Original Set:", fruits)

# 1. Add an element
fruits.add("grapes")
print("\nAfter Adding:", fruits)

# 2. Remove an element
fruits.remove("banana")
print("After Removing Banana:", fruits)

# 3. Discard an element
fruits.discard("pineapple")
print("After Discard:", fruits)

# 4. Length of the set
print("Total Elements:", len(fruits))

# 5. Check if an element exists
print("Is Mango Present?", "mango" in fruits)

# 6. Another set
more_fruits = {"mango", "kiwi", "apple", "papaya"}

# 7. Union
print("\nUnion:", fruits.union(more_fruits))

# 8. Intersection
print("Intersection:", fruits.intersection(more_fruits))

# 9. Difference
print("Difference:", fruits.difference(more_fruits))

# 10. Symmetric Difference
print("Symmetric Difference:", fruits.symmetric_difference(more_fruits))

# 11. Clear the set
fruits.clear()
print("After Clear:", fruits)
