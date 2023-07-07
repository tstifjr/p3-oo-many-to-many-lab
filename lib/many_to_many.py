class Author:
    all = []
    def __init__(self, name) :
        self.name = name
        Author.all.append(self)

    def contracts(self) :
        return [contract for contract in Contract.all if self == contract.author]

    def books(self) :
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties) :
        return Contract(self, book, date, royalties)

    def total_royalties(self) :
        royalties_list = [contract.royalties for contract in self.contracts()]
        return sum(royalties_list)
class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self) :
        return [contract for contract in Contract.all if self == contract.book]

    def authors(self) :
        return [contract.author for contract in self.contracts()]
    
class Contract:
    all = []
    def __init__(self, author, book, date, royalties) :
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author

    def set_author(self,author) :
        if isinstance(author, Author):
            self._author = author
        else :
            raise Exception('Not of Author class')
        
    author = property(get_author, set_author)

    def get_book(self):
        return self._book

    def set_book(self, book) :
        if isinstance(book, Book):
            self._book = book
        else :
            raise Exception('Not of Book class')
        
    book = property(get_book, set_book)

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        if type(date) == str :
            self._date = date
        else :
            raise Exception('Not of string')
    
    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties
    
    def set_royalties(self, royalties):
        if type(royalties) == int :
            self._royalties = royalties
        else :
            raise Exception('Not of int')
    
    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date (cls) :
        return sorted(cls.all, key= lambda ele : ele.date)

