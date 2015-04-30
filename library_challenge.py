class Library(object):
    """Libary with with a dictionary that will contain the shelves. Need to add reporting method to
    list all the books contained."""

    my_library = {}

    def __init__(self, name):
        self.name = name


class Shelf(object):
    """Shelf (that has a dictionary) where a book can be located."""

    row = {}

    def __init__(self, name):
        self.name = name


class Book(object):
    """A book with a given title and author."""

    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    def give_attributes(self):
        """Function to declare book's attibutes."""
        print(self.title, self.author)

    def enshelf(self, shelf_to_remove_from, shelf_to_place_in, book_key):
        """Function to add book to a given shelf."""
        shelf_to_remove_from.row[book_key] = None
        shelf_to_place_in.row[book_key] = self

    def unshelf(self, shelf_to_remove_from, book_key_to_remove):
        """Function to remove book from a given shelf."""
        shelf_to_remove_from.row[book_key_to_remove] = None


if __name__ == '__main__':

    """Instantiate library."""
    grand_central = Library("Grand Central")

    """Instantiate shelf, named Classics, and instantiate 3 books
    to go in it."""

    classics = Shelf("Classics")
    mockingbird = Book("To Kill a Mockingbird", "Harper Lee")
    red_badge = Book("Red Badge of Courage", "Stephen Crane")
    art_of_war = Book("The Art of War", "Sun Tzu")

    """Insert shelf, classics, into the library, grand_central."""

    grand_central.my_library["class"] = classics

    """Insert 3 books into the shelf, Classics."""

    grand_central.my_library["class"].row["Book1"] = mockingbird
    grand_central.my_library["class"].row["Book2"] = red_badge
    grand_central.my_library["class"].row["Book3"] = art_of_war

    """Instantiate shelf, named Fantasy, and instantiate 2 books
    to be stored in it."""

    fantasy = Shelf("Fantasy")
    potter = Book("Harry Potter and the Order of the Phoenix", "J.K. Rowling")
    lord_of_the_rings = Book(
        "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien"
    )

    """Insert shelf, fantasy, in the library, grand_central."""

    grand_central.my_library["fant"] = fantasy

    """Insert 2 books into the shelf, fantasy."""

    grand_central.my_library["fant"].row["Book4"] = potter
    grand_central.my_library["fant"].row["Book5"] = lord_of_the_rings

    """Print the values of the shelf dict. to make sure it works."""

    # print(classics.row["Book1"].title)

    # print(grand_central.my_library.get("fant").row["Book1"].give_attributes())

    # """Move book, lord_of_the_rings to shelf, classics."""
    # lord_of_the_rings.enshelf(fantasy, classics, "Book10")

    # print(classics.row["Book10"].give_attributes())

    # lord_of_the_rings.unshelf(classics, "Book10")  # This removes the book, but there needs to be a better way.

    # print(classics.row["Book10"].title)

    # print(grand_central.my_library["class"].row.get("Book1").author)
    # print(grand_central.my_library["fant"].row.get("Book5").author)

    # grand_central.my_library["class"].row["Book11"] = potter

    #for key, value in grand_central.my_library.iteritems():
    for key, value in grand_central.my_library["class"].row.iteritems():
        print(key, value.title)
