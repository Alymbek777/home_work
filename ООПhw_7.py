
import sqlite3

connect = sqlite3.connect("bk.db")
cursor = connect.cursor()

cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY,
               title VARCHAR(255),
               author VARCHAR(255),
               year INTEGER
)""")
               
class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.year = None

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

    def add_book(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        cursor.execute(f"""INSERT INTO books(title,author,year) VALUES('{self.title}', '{self.author}', {self.year})  """)
        connect.commit()

    def update_book(self,new_title,new_author,new_year):
        self.title = new_title
        self.author = new_author
        self.year = new_year
        cursor.execute(f"UPDATE books SET author = '{new_author}', year = {new_year} WHERE title = '{new_title}'")
        connect.commit()
        print(f"Вы успешно обновили информацию о книгах ")

    def delete_book(self,delete_title):
        self.title = delete_title
        cursor.execute(f"DELETE FROM books WHERE title = '{delete_title}'")
        connect.commit()
        print("Вы успешно удалили")
    def main(self):
        while True:
            user = input("1 -Просматривать информацию о книгах, 2 - Добавлять новые книги, 3 - Обновлять информацию, 4 - Удалять книги: ")
            if user == "1":
                self.display_info()
            elif user == "2":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                print(f"Вы успешно добавили книгу в базу данных")
                self.add_book(title,author,year)
            elif user == "3":
                new_title = input("Введите название книги, которую хотите обновить: ")
                new_author = input("Введите автора книги: ")
                new_year = int(input("Введите год издания книги: "))
                self.update_book(new_title,new_author,new_year)
            elif user == "4":
                delete_title = input("Введите название книги, которую хотите удалить: ")
                self.delete_book(delete_title)


book = Book()
book.add_book("Тарас и Бульба","Гоголь",1677)
book.add_book("Евгений Онегин","Пушкин",1812)
book.main()








