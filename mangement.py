from abc import ABC,abstractmethod
class Book:
    def __init__(self,book_id,book_title,author,total_num):
        self.book_id = book_id
        self. book_title = book_title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):
        self.__available_num += 1

    def get_available_num(self):
        return self.__available_num

class Member(ABC):
    def __init__(self,member_id,name,password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrow_books = []

    def borrow_book(self,book:Book):
        if len(self.__borrow_books) >= self.get_max_book():
            print("失败")
            return False

        if book.borrow_book():
            self.__borrow_books.append(book)
            print(f"{self.name}成功借阅{book.book_title}")
            return True
        else:
            print(f"{book.book_title}借阅失败")
            return False

    @abstractmethod
    def get_max_book(self) -> int:
        pass

    def return_book(self,book:Book):
        if book in self.__borrow_books:
            book.return_book()
            self.__borrow_books.remove(book)
            print(f"{self.name}已成功归还{book.book_title}")
            return True
        else:
            print(f"{book.book_title}借阅失败")
            return False

    def get_password(self):
        return  self.__password

    def get_borrow_books(self):
        return self.__borrow_books

class NormalMember(Member):
    def get_max_book(self) -> int:
        return 3

class VipMember(Member):
    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level

    def get_max_book(self) -> int:
        return 6 + self.vip_level

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []