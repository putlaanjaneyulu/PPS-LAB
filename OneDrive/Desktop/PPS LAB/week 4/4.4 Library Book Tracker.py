n = int(input("number of books: "))


books = []
for _ in range(n):
    title, author, year, copies = input().split()
    year = int(year)
    copies = int(copies)
    books.append((title, author, year, copies))

start_year, end_year = map(int, input().split())

result = [book for book in books if start_year <= book[2] <= end_year]

if result:
    for book in result:
        print(book)

else:
    print("No books found in the given range.")
