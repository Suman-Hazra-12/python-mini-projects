
class Book:
    def __init__(self, title: str, author : str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")



class Library:
    def __init__(self):
        self.books = []

    def add_book(self, books: Book):
        self.books.append(books)
        print(f"Book '{books.title}' added to the library.")

    def search_by_title(self, title: str):
        print(f"Searching for books with title '{title}':")
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                found = True
        if not found:
            print("No book found with that title.")

    def search_by_author(self, author):
        print(f"Searching for books by author '{author}':")
        found = False
        for book in self.books:
            if book.author.lower() == author.lower():
                book.display_info()
                found = True
        if not found:
            print("No book found by that author.")

    def display_all_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                book.display_info()



if __name__ == "__main__":
    library = Library()

    
    library.add_book(Book("The Alchemist", "Paulo Coelho", "Fiction"))
    library.add_book(Book("Sapiens", "Yuval Noah Harari", "History"))
    library.add_book(Book("1984", "George Orwell", "Dystopian"))

   
    library.display_all_books()

  
    library.search_by_title("1984")

    library.search_by_author("Paulo Coelho")
