class Library(object):
    """Libary with 3 empty shelves (lists). Need to add reporting method to
    list all the books contained."""

    shelf_1 = []
    shelf_2 = []
    shelf_3 = []

    def __init__(self, name):
        self.name = name


class Shelf(object):
    """Shelf with 3 slots (that are dicts.) that a book can be located."""
    slot_1 = {}
    slot_2 = {}
    slot_3 = {}

    def __init__(self, name):
        self.name = name


class Book(object):
    """A book with a given title."""
    def __init__(self, title):
        self.title = title


if __name__ == '__main__':

    """Instantiate library."""
    grand_central = Library("Grand Central")

    """Instantiate shelf, named Classics, and instantiate 3 books
    to go in it."""

    classics = Shelf("Classics")
    mockingbird = Book("To Kill a Mockingbird")
    red_badge = Book("Red Badge of Courage")
    art_of_war = Book("The Art of War")

    """Insert 3 books into the shelf, Classics."""

    classics.slot_1["Book1"] = mockingbird
    classics.slot_2["Book2"] = red_badge
    classics.slot_3["Book3"] = art_of_war

    """Print the values of the dict. to make sure it works."""

    print(classics.slot_1["Book1"].title)
    print(classics.slot_2["Book2"].title)
    print(classics.slot_3["Book3"].title)
