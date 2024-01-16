import random
from date_class import Date


class Library:

    # A constructor to initialize the library
    def __init__(self, max_days=10, penalty=10):
        self.__books = {}
        self.__maxDays = max_days
        self.__penalty = penalty
        self.token_person_books = {}

    @staticmethod
    def token_gen():
        token = Library.ran_hash(random.randint(3, 5)) + \
            Library.ran_hash(random.randint(3, 5))
        return token

    @staticmethod
    def ran_hash(n) -> str:
        return ''.join([chr(random.randint(33, 126)) for _ in range(n)])

    # This is a private function called only from within the function
    def __issue_book(self, book, person, date_of_issue) -> str:
        self.__books[book] -= 1
        self.token_person_books[token] = (book, person, date_of_issue)
        token = Library.token_gen()
        return token

    # This function adds a specified quantity of a book in the library
    def add_book(self, book, quantity=1):
        if book in self.__books:
            self.__books[book] += quantity
        else:
            self.__books[book] = quantity

    # This function check whether we keep a specific book and is it in stock and
    # returns its availability
    def search_book(self, book):
        if book not in self.__books:
            return 0  # we dont keep this book
        elif self.__books[book] == 0:
            return -1  # we currently dont have this book
        return 1  # we have this book in the library

    # Issue a request for a book and issue it to the user if it is available
    def issue_request(self, book, person, curr_date):
        if self.search_book(book) == 1:
            print("Book available")
            token_numer = self.__issue_book(book, person, curr_date)
            print(
                f"Book issued to {person.name} on {self.token_person_books[token_numer][-1].date} and it must be returned or reissued by {self.token_person_books[book][-1].add_days(self.__maxDays).date} otherwise {self.__penalty}Rs will be charged per day.")
        elif self.search_book(book) == -1:
            print(f"Unfortunately the book {book} is currently unavailable")
        else:
            print(f"Sorry but we don't keep the book {book}.")

    def return_or_reissue_book(self, token, date_of_return, book_return=1):
        person = self.token_person_books[token][1]
        date_of_issue = self.token_person_books[token][-1]
        book = self.token_person_books[token][0]
        num_days = Date.diff(date_of_return, date_of_issue)
        if self.__maxDays < num_days:
            print(
                f'You have to pay a fine of Rs{(num_days-self.__maxDays)*self.__penalty}')
        if book_return == 1:
            print('Your book has been returned')
        else:
            # continue from here
            print(
                f'The book {book} has been reissued with the same token_number')
        pass
