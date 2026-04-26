
books = ["The Alchemist", "1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"]


print("Original list of books:", books)


books.remove("1984")
print("After selling '1984':", books)


books.append("Pride and Prejudice")
books.append("The Catcher in the Rye")
print("After adding new books:", books)


print("Total number of books:", len(books))


print("First book:", books[0])
print("Last book:", books[-1])

sorted_books = sorted(books)
print("Books sorted alphabetically:", sorted_books)




if "Moby Dick" in books:
    print("Yes, 'Moby Dick' is available in the store")

    
else:
    print("No, 'Moby Dick' is not available in the store")
