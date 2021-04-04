M = int(input())
N = int(input())
library_books = []
book_list = []

for i in range(M):
    library_books.append(input())
for i in range(N):
    book_list.append(input())

for book in book_list:
    is_found = False
    for lb in library_books:
        if lb == book:
            is_found = True
    if is_found:
        print("YES")
    else:
        print("NO")
