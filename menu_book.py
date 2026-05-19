import time
from book import *
def menu():
    saved=True
    while True:
        print('~~~~~~~~~~~~МЕНЮ~~~~~~~~~~~~')
        print('1 - загрузка RAM из файла')
        print('2 - сохранение RAM в файл')
        print('3 - просмотр всех записей')
        print('4 - добавление новой записи')
        print('5 - поиск записи (по разным критериям)')
        print('6 - редактирование записи')
        print('7 - удаление записи')
        print('8 - сортировка (по разным полям)')
        print('9 - экспорт в CSV')
        print('10 - выход')
        print('11 - настройки')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        time.sleep(1)
        choice=input('🟢 Выбор: ')



        if choice=='1':
            file_name=input('Введите имя файла: ')
            load_from_file(file_name)
        elif choice=='2':
            saved=True
            file_name=input('Введите имя файла: ')
            save_to_file(file_name)
        elif choice=='3':
            check_books()
        elif choice=='4':
            saved=False
            add_book()
        elif choice=='5':
            search()
        elif choice=='6':
            saved=False
            edit_book()
        elif choice=='7':
            saved=False
            delete_book()
        elif choice=='8':
            saved=False
            sort_books()
        elif choice=='9':
            export_to_csv()
        elif choice=='10':
            exit(saved)
        elif choice=='11':
            settings()
        else:
            print('❌ Неверный выбор!')