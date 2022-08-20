from models import (Base, session,
                    Book, engine)

import datetime
import csv


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1. Add a book
        \r2. Search for a book
        \r3. Update a book
        \r4. Delete a book
        \r5. List all books
        \r6. Quit
        ''')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            list_books()
        elif choice == '6':
            print('\nGoodbye!')
            break
        else:
            print('\nPlease enter a valid choice')
            continue


def app():
    app_running = True
    while app_running:
        menu()
        choice = input('\nWould you like to continue? (y/n): ')
        if choice == 'y':
            continue
        else:
            app_running = False
            print('\nGoodbye!')
            break


def add_book():
    title = input('\nEnter the title of the book: ')
    author = input('Enter the author of the book: ')
    published = input('Enter the date the book was published: ')
    price = input('Enter the price of the book: ')
    format = input('Enter the format of the book: ')
    book = Book(title=title, author=author, published=published,
                price=price, format=format)
    session.add(book)
    session.commit()
    print('\nThe book has been added!')


def search_book():
    title = input('\nEnter the title of the book: ')
    book = session.query(Book).filter_by(title=title).first()
    if book:
        print(book)
    else:
        print('\nThat book is not in the database.')


def update_book():
    title = input('\nEnter the title of the book: ')
    book = session.query(Book).filter_by(title=title).first()
    if book:
        print(book)
        new_title = input('\nEnter the new title of the book: ')
        book.title = new_title
        session.commit()
        print('\nThe book has been updated!')
    else:
        print('\nThat book is not in the database.')


def delete_book():
    title = input('\nEnter the title of the book: ')
    book = session.query(Book).filter_by(title=title).first()
    if book:
        session.delete(book)
        session.commit()
        print('\nThe book has been deleted!')
    else:
        print('\nThat book is not in the database.')


def list_books():
    books = session.query(Book).all()
    for book in books:
        print(book)


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
    date_list = date_str.replace(',', '').split(' ')
    # print(date_list)
    month = int(months.index(date_list[0]) + 1)
    day = int(date_list[1].split(',')[0])
    # print(day)
    year = int(date_list[2])
    return datetime.date(year, month, day)


def clean_price(price):
    price = float(price.replace('$', ''))
    return int(price * 100)
    # print(price)


def add_csv():
    with open('suggested_books.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            book_in_db = session.query(Book).filter_by(title=row[0]).one_or_none()
            if book_in_db is None:
                book = Book(title=row[0], author=row[1], published=clean_date(row[2]),
                            price=clean_price(row[3]), format=row[4])
                session.add(book)
        session.commit()
    print('\nThe books have been added!')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # menu()
    add_csv()
    # clean_price('29.99')
    for book in session.query(Book).all():
        print(book)
