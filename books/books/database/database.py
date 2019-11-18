import sqlite3
import pprint


def create_books_table():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()

    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                                                id integer PRIMARY KEY,
                                                book_title text,
                                                author text,
                                                publish_date date,
                                                publisher text,
                                                selling_price numeric
                                                )""")
    connection.commit()
    connection.close()


create_books_table()


def create_books():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""INSERT INTO books (book_title, author, publish_date, publisher, selling_price) 
                      VALUES("Pavadinimas", "Autorius", "Data", "Kiekis", 10)""")
    connection.commit()
    connection.close()


create_books()


def get_all_books():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    books = connection_cursor.execute("SELECT * FROM books")

    for row in books:
        print(row)

    connection.close()


get_all_books()


def get_books():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    for row in cursor.execute("SELECT * FROM books"):
        print(row)

    connection.close()


get_books()


def update_books_title(new_value, book_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET book_title = ? WHERE id = ?""")
    update_data = [new_value, book_id]
    connection.commit()
    connection.close()


def update_books_publisher(new_value, book_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET publisher = ? WHERE id = ?""")
    update_data = [new_value, book_id]
    connection.commit()
    connection.close()


def update_books_author(new_value, book_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET author = ? WHERE id = ?""")
    update_data = [new_value, book_id]
    connection.commit()
    connection.close()


def update_books_publish_date(new_value, book_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET publish_date = ? WHERE id = ?""")
    update_data = [new_value, book_id]
    connection.commit()
    connection.close()


def update_books_selling_price(new_value, book_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET selling_price = ? WHERE id = ?""")
    update_data = [new_value, book_id]
    connection.commit()
    connection.close()


def delete_books_by_id(books_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""DELETE FROM books WHERE id = ?""")
    entry_id = [books_id]
    connection.commit()
    connection.close()


def create_publishers_table():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()

    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS publishers(
                                                 id integer PRIMARY KEY,
                                                        publisher_name text,
                                                        book_title text,
                                                        author text,
                                                        printed_quantity integer,
                                                        printing_price integer
                                                )""")
    connection.commit()
    connection.close()


create_publishers_table()


def create_publisher():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""INSERT INTO publishers (publisher_name, book_title, author, printed_quantity, printing_price) 
                      VALUES("Leidejo Pavadinimas", "Pavadinimas", "Autorius", 50, 15)""")
    connection.commit()
    connection.close()


create_publisher()


def get_publishers():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    for row in cursor.execute("SELECT * FROM publishers"):
        print(row)

    connection.close()


get_publishers()


def update_publisher_name(new_value, publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE publishers SET publisher_name = "Pavadinimas" WHERE id = ?""")
    update_data = [new_value, publisher_id]
    connection.commit()
    connection.close()


def update_publisher_book_title(new_value, publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE books SET publisher = ? WHERE id = ?""")
    update_data = [new_value, publisher_id]
    connection.commit()
    connection.close()


def update_publisher_author(new_value, publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE publishers SET author = ? WHERE id = ?""")
    update_data = [new_value, publisher_id]
    connection.commit()
    connection.close()


def update_publisher_printed_quantity(new_value, publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE publishers SET printed_quantity = ? WHERE id = ?""")
    update_data = [new_value, publisher_id]
    connection.commit()
    connection.close()


def update_publisher_printing_price(new_value, publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""UPDATE publishers SET printing_price = ? WHERE id = ?""")
    update_data = [new_value, publisher_id]
    connection.commit()
    connection.close()


def delete_publisher_by_id(publisher_id):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""DELETE FROM publishers WHERE id = ?""")
    entry_id = [publisher_id]
    connection.commit()
    connection.close()


def books_profit():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    profit = connection_cursor.execute("""SELECT ((printing_price - selling_price) * printed_quantity) 
                                        FROM books JOIN publishers ON books.book_title = publishers.book_title 
                                        WHERE books.id = 1;""")

    for row in profit:
        print(row)

    connection.close()

books_profit()
