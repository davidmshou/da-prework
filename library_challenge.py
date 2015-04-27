class Library(object):
    """Libary with with a dictionary that will contain the shelves. Need to add reporting method to
    list all the books contained."""

    my_library = {}  # Want these to become 1 library that will hold all of my shelves.

    def __init__(self, name):
        self.name = name


class Shelf(object):
    """Shelf with a slot (that has a dictionary) that a book can be located."""

    row = {}

    def __init__(self, name):
        self.name = name


class Book(object):
    """A book with a given title and author."""

    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    """Function to declare books attibutes."""
    def give_attributes(self):
        print(self.title, self.author)


if __name__ == '__main__':

    """Instantiate library."""
    grand_central = Library("Grand Central")

    """Instantiate shelf, named Classics, and instantiate 3 books
    to go in it."""

    classics = Shelf("Classics")
    mockingbird = Book("To Kill a Mockingbird", "Harper Lee")
    red_badge = Book("Red Badge of Courage", "Stephen Crane")
    art_of_war = Book("The Art of War", "Sun Tzu")

    """Insert 3 books into the shelf, Classics."""

    classics.row["Book1"] = mockingbird
    classics.row["Book2"] = red_badge
    classics.row["Book3"] = art_of_war

    """Insert shelf, classics, into the library, grand_central."""

    grand_central.my_library["class"] = classics

    """Instantiate shelf, named Fantasy, and instantiate 2 books
    to be stored in it."""

    fantasy = Shelf("Fantasy")
    potter = Book("Harry Potter and the Order of the Phoenix", "J.K. Rowling")
    lord_of_the_rings = Book(
        "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien"
    )

    """Insert 2 books into the shelf, fantasy."""

    fantasy.row["Book4"] = potter
    fantasy.row["Book5"] = lord_of_the_rings

    """Insert shelf, fantasy, in the library, grand_central."""

    grand_central.my_library["fant"] = fantasy

    """Print the values of the shelf dict. to make sure it works."""

    print(classics.row["Book1"].title)
    # print(classics.slot_2["Book2"].title)
    # print(classics.slot_3["Book3"].title)

    # print(grand_central.my_library.get("class").classics.values())

    print(grand_central.my_library.get("fant").row["Book1"].give_attributes())

    # print(grand_central.my_library["class"].row.get("Book1").author)
    # print(grand_central.my_library["fant"].row.get("Book5").author)
