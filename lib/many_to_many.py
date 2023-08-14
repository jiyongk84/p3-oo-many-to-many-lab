from datetime import datetime

class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def authors(self):
        authors = set()
        for contract in self.contracts_list:
            authors.add(contract.author)
        return list(authors)

class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def books(self):
        books = set()
        for contract in self.contracts_list:
            books.add(contract.book)
        return list(books)

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        if not isinstance(book, Book):
            raise ValueError("Book must be of type Book")
        if not isinstance(date, str):
            raise ValueError("Date must be of type str")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be of type int")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.contracts_list.append(self)
        book.contracts_list.append(self)
        Contract.all.append(self)
        
    @classmethod
    def contracts_by_date(cls):
        sorted_contracts = sorted(cls.all, key=lambda contract: contract.date)
        return sorted_contracts


