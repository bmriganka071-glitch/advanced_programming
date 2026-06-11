from abc import ABC, abstractmethod

class LibraryItem(ABC):
    count = 0

    def __init__(self, title, year):
        self.set_title(title)
        self.set_year(year)
        LibraryItem.count += 1

    def get_title(self):
        return self.title

    def set_title(self, title):
        if title is None or title.strip() == "":
            self.title = "Unknown"
        else:
            self.title = title

    def get_year(self):
        return self.year

    def set_year(self, year):
        if year > 0:
            self.year = year
        else:
            self.year = 0

    @staticmethod
    def get_count():
        return LibraryItem.count

    @abstractmethod
    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.set_author(author)

    def get_author(self):
        return self.author

    def set_author(self, author):
        if author is None or author.strip() == "":
            self.author = "Unknown"
        else:
            self.author = author

    def display_info(self):
        print(f"{self.get_title()}, (Year-{self.get_year()}) by {self.get_author()}")


class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre):
        super().__init__(title, year)
        self.set_duration(duration)
        self.set_genre(genre)

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        if duration > 0:
            self.duration = duration
        else:
            self.duration = 0

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        if genre is None or genre.strip() == "":
            self.genre = "Unknown"
        else:
            self.genre = genre

    def display_info(self):
        print(f"{self.get_title()} ,(Year-{self.get_year()}), {self.get_genre()}, {self.get_duration()} mins")


if __name__ == "__main__":
    items = []

    print("------ LIBRARY ITEMS ------\n")
    items.append(Book("Sapiens: A Brief History of Humankind", 2011, "Yuval Noah Harari"))
    items.append(Book("The Pragmatic Programmer", 1999, "Andrew Hunt"))
    items.append(Book("Clean Code", 2008, "Robert C. Martin"))

    print("___________BOOKS___________")
    for item in items:
            item.display_info()

    print("\n")
            
    items=[]
    items.append(DVD("Interstellar", 2014, 169, "Sci-Fi"))
    items.append(DVD("The Dark Knight", 2008, 152, "Action"))
    items.append(DVD("Forrest Gump", 1994, 142, "Drama"))

    print("_________DVDS_____________")
    for item in items:
        item.display_info()
     

    print(f"\nTotal items in library: {LibraryItem.get_count()}")