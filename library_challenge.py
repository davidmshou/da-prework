class Library(object):
    """Libary with with a dictionary that will contain shelves."""

    my_library = {}

    def __init__(self, name):
        self.name = name

    def report_books(self):
        num_books = 0
        print("\n")
        print("The books contained in this library are as follows: \n")
        for key, shelf in grand_central.my_library.iteritems():
            for book in shelf:
                num_books += 1
                print(book)
        print("\n")
        return("In total, this library contains %i books. \n") % (num_books)
        # return num_books


class Shelf(dict):
    """Shelf (that inherits from dict.) where a book can be located."""

    def __init__(self, name):
        self._dict = {}
        self.name = name

    def report_contents(self, key_to_report):
        print("The contents of the %s shelf are as follows:" % (key_to_report))
        for key, value in grand_central.my_library[key_to_report].iteritems():
            print(key, value.author)
        return("Thank you.")

    # row = {}

    # def __init__(self, name):
    #     self.name = name


class Book(object):
    """A book with a given title and author."""

    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    def give_attributes(self):
        """Function to declare book's attibutes."""
        print(self.title, self.author)

    def enshelf(self, shelf_to_place_in, book_key):
        """Function to add book to a given shelf."""
        # del shelf_to_remove_from[book_key]
        shelf_to_place_in[book_key] = self

    def unshelf(self, shelf_to_remove_from, book_key_to_remove):
        """Function to remove book from a given shelf."""
        del shelf_to_remove_from[book_key_to_remove]


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

    grand_central.my_library["classics"] = classics

    """Insert 3 books into the shelf, Classics."""

    grand_central.my_library["classics"]["To Kill a Mockingbird"] = mockingbird
    grand_central.my_library["classics"]["Red Badge of Courage"] = red_badge
    grand_central.my_library["classics"]["The Art of War"] = art_of_war

    """Instantiate shelf, named Fantasy, and instantiate 2 books
    to be stored in it."""

    fantasy = Shelf("Fantasy")
    potter = Book("Harry Potter and the Order of the Phoenix", "J.K. Rowling")
    lord_of_the_rings = Book(
        "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien"
    )

    """Insert shelf, fantasy, in the library, grand_central."""

    grand_central.my_library["fantasy"] = fantasy

    """Insert 2 books into the shelf, fantasy."""

    grand_central.my_library["fantasy"]["Harry Potter and the Order of the Phoenix"] = potter
    grand_central.my_library["fantasy"]["The Lord of the Rings: The Fellowship of the Ring"] = lord_of_the_rings

    """Print the values of the shelf dict. to make sure it works."""

    """
    Move book, lord_of_the_rings to shelf, classics, from the shelf, fantasy.
    """
    lord_of_the_rings.enshelf(
        classics, "The Lord of the Rings: The Fellowship of the Ring"
    )
    lord_of_the_rings.unshelf(
        fantasy, "The Lord of the Rings: The Fellowship of the Ring"
    )

    """Remove book, lord_of_the_rings, from shelf, classics."""
    lord_of_the_rings.unshelf(
        classics, "The Lord of the Rings: The Fellowship of the Ring"
    )

    """
    Return book, lord_of_the_rings to both fantasy and classics,
    because it is :P
    """
    lord_of_the_rings.enshelf(
        classics, "The Lord of the Rings: The Fellowship of the Ring"
    )
    lord_of_the_rings.enshelf(
        fantasy, "The Lord of the Rings: The Fellowship of the Ring"
    )

    """Calling function to report all books within the library."""
    print(grand_central.report_books())

    """Calling functions to print contents of each shelf."""
    print(classics.report_contents("classics"))
    print(fantasy.report_contents("fantasy"))

    # for key, value in grand_central.my_library.iteritems():
    # for key, value in grand_central.my_library["fant"].iteritems():
    #     print(key, value.author)
