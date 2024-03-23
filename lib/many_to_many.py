from datetime import datetime

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        Author.members.append(self)
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    members = []

    def __init__(self, title):
        self.title = title
        Book.members.append(self)
        
    @classmethod
    def all_books(cls):
        return cls.members
    

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))



class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date  # Ensure date format is consistent and allows correct sorting
        self.royalties = royalties
        Contract.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        target_date = datetime.strptime(date, "%d/%m/%Y")  # Convert target date string to datetime object
        sorted_contracts = sorted(cls.members, key=lambda x: datetime.strptime(x.date, "%d/%m/%Y"))
        return [contract for contract in sorted_contracts if datetime.strptime(contract.date, "%d/%m/%Y") == target_date]
