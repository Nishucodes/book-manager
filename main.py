from book import Book

b1 = Book("Python Guide", "Mohit", 300)
b2 = Book("C++ Mastery", "Aliza", 250)

print(b1)
print("Same title?", b1 == b2)
print("Pages combined:", b1 + b2)
print("Bigger book:", b1 if b1 > b2 else b2)