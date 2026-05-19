class Book:
    counter=0
    def __init__(self,name,author,year_of_publication,isbn,genre,pages):
        self.name=name
        self.author=author
        self.year_of_publication=year_of_publication
        self.isbn=isbn
        self.genre=genre
        self.pages=pages
        Book.counter+=1
        self.id=Book.counter
        print(f"Добавление книги (в RAM) с ID: {self.id}")


    def __str__(self):
        return (f'~~~~~~~~~Книга~~~~~~~~~\nНазвание: {self.name}\nАвтор: {self.author}\nГод издания: {self.year_of_publication}\nISBN: {self.isbn}\nЖанр: {self.genre}\nКоличество страниц: {self.pages}\nID книги: {self.id}\n~~~~~~~~~~~~~~~~~~~~~~~')
    def __repr__(self):
        return (f"Book(name='{self.name}',author='{self.author}', "
                f"year_of_publication={self.year_of_publication},isbn='{self.isbn}', "
                f"genre='{self.genre}',pages={self.pages}, "
                f"id={self.id})")


    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Название иметь формат строки")
        self.name = value

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Автор иметь формат строки")
        self.author = value

    @year_of_publication.setter
    def year_of_publication(self, value):
        if not isinstance(value, int):
            raise ValueError("Год издания должен быть натуральным числом")
        if value<=0:
            raise ValueError("Год издания должен быть натуральным числом")
        self.year_of_publication = value

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise ValueError("ISBN иметь формат строки")
        self.isbn = value

    @genre.setter
    def genre(self, value):
        if not isinstance(value, str):
            raise ValueError("Название иметь формат строки")
        self.genre = value


    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Кол-во страниц должно быть натуральным числом")
        if value <= 0:
            raise ValueError("Кол-во страниц должно быть натуральным числом")
        self.pages = value

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.name.lower() == other.name.lower()

    def __ne__(self, other):
        if not isinstance(other, Book):
            return True
        return self.name.lower() != other.name.lower()

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year_of_publication <= other.year_of_publication

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages >= other.pages

    def __copy__(self):
        return Book(
            self.name,
            self.author,
            self.year_of_publication,
            self.isbn,
            self.genre,
            self.pages
        )
    def __del__(self):
        print(f'Удаление книги (из RAM) с ID: {self.id}')




books=[]
deleted_books=[]







def exit(saved):
    if saved:
        print('✅ Успешный выход!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return
    else:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n❗ Вы не сохранили текущие изменения. При выходе они будут утеряны. Вы уверены, что хотите завершить работу программы?')
        choice = input('Выбор(да/нет): ')
        if choice.lower() == 'да':
            print('✅ Успешный выход!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            return

def check_books():
    if not (books):
        print('⛔ БД пустая')
    else:
        for book in books:
            print(book)
def load_from_file(file_name):
    if books:
        print('❗ При открытии файла текущие изменения будут утеряны. Вы уверены, что хотите открыть файл?')
        choice = input('Выбор(да/нет): ')
        if choice.lower() == 'да':
            pass
        else:
            return
    deleted_books.extend(books)
    books.clear()
    try:
        with open(file_name,'r',encoding='UTF-8') as file_r:
            for string in file_r:
                if not string.strip():
                    continue
                try:

                    data=string.strip().split(';')
                    book=Book(data[0],data[1],
                                  int(data[2]),
                                  data[3],data[4],
                                  int(data[5]))
                    books.append(book)
                except ValueError:
                    print(f'❌ Ошибка чтения строки: {string}')
                    books.clear()
                    return
            print('✅ Книги успешно загружены!')
    except FileNotFoundError:
        print('❌ Файл не найден')
        return


def save_to_file(file_name):
    with open(file_name,'w',encoding='UTF-8') as file_w:
        for book in books:
            file_w.write(f'{book.name};{book.author};{book.year_of_publication};{book.isbn};{book.genre};{book.pages}\n')
        print(f'✅ Книги успешно сохранены!')

def add_book():
    name=input('Введите название книги: ')
    author = input_('Введите ФИО автора книги: ')
    year_of_publication = input('Введите год издания книги: ')
    isbn = input('Введите ISBN: ')
    genre = input('Введите жанр книги: ')
    pages = input('Введите количество страниц: ')

    book=Book(name,author,year_of_publication,isbn,genre,pages)
    books.append(book)
    print(f'✅ Книга {book.name} с ID {book.id} успешно создана!')

def delete_book():
    print('~~~~~~~~~~~~МЕНЮ УДАЛЕНИЯ~~~~~~~~~~~~')
    print('1 - удаление по названию книги')
    print('2 - удаление по ID книги')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    choice = input('Выбор: ')
    if choice=='1':
        name=input('Введите название книги для удаления: ')
    elif choice=='2':
        id=input('Введите ID книги для удаления: ')
    else:
        print("❌ Неверный выбор")
        return

    key=False
    copy_books=books.copy()
    for book in copy_books:
        if choice=='1':
            if book.name.lower() == name.lower():
                deleted_books.append(book)
                books.remove(book)
                key=True



        elif choice=='2':
            if str(book.id) == id:
                deleted_books.append(book)
                books.remove(book)
                print(f"✅ Книга успешно удалена с ID {id}")
                return
    if key:
        print(f"✅ Книг(а/и) с названием: '{name}'  успешно удален(а/ы)")
        return
    print("❌ Книга для удаления не найдена")

def edit_book():
    id=input('Введите ID книги для изменения параметров: ')

    for book in books:
        if str(book.id)==id:
            print('Введите новые данные книги')
            print()
            book.name=input_('Название: ')
            book.author=input_('ФИО автора: ')
            book.year_of_publication=input('Год издания: ')
            book.isbn=input('ISBN: ')
            book.genre=input('Жанр: ')
            book.pages = input('Количество страниц: ')
            print()
            print('✅ Книга успешно изменена')
            return
    print("❌ Книга не найдена")

def search():
    print('~~~~~~~~~~~~МЕНЮ ПОИСКА~~~~~~~~~~~~')
    print('1 - поиск по названию книги')
    print('2 - поиск по жанру книги')
    print('3 - поиск по автору книги')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    choice=input('Выбор: ')
    found=False

    if choice=='1':
        name=input('Введите название книги: ')

        for book in books:
            if book.name.lower()==name.lower():
                print(book)
                found=True

    elif choice=='2':
        genre=input('Введите жанр книги: ')

        for book in books:
            if book.genre.lower()==genre.lower():
                print(book)
                found=True
    elif choice=='3':
        author = input('Введите автора книги: ')

        for book in books:
            if book.author.lower() == author.lower():
                print(book)
                found = True
    else:
        print("❌ Неверный выбор")
        return
    if not found:
        print('⛔ Ничего не найдено')


def sort_books():
    if not books:
        print("⛔ БД пустая")
        return
    print("~~~~~~~~~~~~СОРТИРОВКА~~~~~~~~~~~~")
    print("1 - по количеству страниц")
    print("2 - по году издания")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice = input("Выбор: ")
    n = len(books)
    for i in range(n):
        for j in range(n-i-1):
            if choice=='1':
                condition=books[j]>books[j+1]
            elif choice=='2':
                condition=not(books[j]<=books[j+1])
            else:
                print("❌ Неверный выбор")
                return

            if condition:
                books[j], books[j + 1] = books[j + 1], books[j]

    print("✅ Книги успешно отсортированы")

def export_to_csv():
    print('❗ВНИМАНИЕ!\n1)Формат .csv сохраняет данные без учета форматирования.\n2)Если файл с данным названием существует, то он должен быть закрыт.')

    time.sleep(1)

    answers_of_agreement=('да','y','д','yes','yeah','yep','ознакомился','ознакомилась','ознакомилось','пойдет','го','все ок','ок','jr','lf')
    choice=input('Вы подтверждаете, что ознакомились с предупреждением? Да/нет: ')

    if choice.lower() in answers_of_agreement:
        pass
    else:
        return
    name=input('Введите название файла для экспорта в CSV: ')
    if not name.endswith('.csv'):
        name+='.csv'
    with open(name, 'w', encoding='UTF-8-SIG') as file_w:

        file_w.write("name\tauthor\tyear_of_publication\tisbn\tgenre\tpages\n")

        for book in books:
            file_w.write(f"{book.name}\t{book.author}\t{book.year_of_publication}\t{book.isbn}\t{book.genre}\t{book.pages}\n")

    print("✅ Экспорт в CSV завершён")



def settings():
    print('~~~~~~~~~~~~НАСТРОЙКИ~~~~~~~~~~~~')
    print('1 - просмотр удаленных книг')
    print('2 - назад')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    choice=input('Выбор: ')
    if choice=='1':
        if not(deleted_books):
            print('❌ Нет удаленных книг!')
        for del_book in deleted_books:
            print(del_book)
    elif choice=='2':
        pass
    else:
        print('❌ Неверный выбор!')
        return settings()
