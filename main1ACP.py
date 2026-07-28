books = ["The Alchemist", "Harry Potter", "The Hobbit", "1984", "Wings of Fire"]
print("Book List:", books)

print("Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Atomic Habits")
print("\nAfter Adding a Book:", books)

books.remove("1984")
print("After Removing a Book:", books)

books.sort()
print("Books in Alphabetical Order:", books)

books.reverse()
print("Books in Reverse Order:", books)

librarian = {
    "name": "Mrs. Priya",
    "library": "City Library",
    "experience": 8
}

print("\nLibrarian Details:", librarian)

print("Library Name:", librarian["library"])
print("Experience:", librarian.get("experience", "Not Found"))

librarian["experience"] = 9
librarian["email"] = "priya@library.com"
librarian.pop("experience")

print("Updated Librarian Details:", librarian)

book_ids = [101, 102, 103, 104, 105]
book_names = [
    "The Alchemist",
    "Harry Potter",
    "The Hobbit",
    "Wings of Fire",
    "Atomic Habits"
]

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:", book_directory)
print("Book with ID 103:", book_directory[103])
