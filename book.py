class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"📘 '{self.title}' by {self.author} ({self.pages} pages)"

    def __add__(self, other):
        return f"Combined pages: {self.pages + other.pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.pages > other.pages