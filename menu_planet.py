import handler_planets
import time
def menu():
    saved = True
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
        choice=input('🟢Выбор: ')




        if choice=='1':

            file_name=input('Введите имя файла: ')
            handler_planets.load_from_file(file_name)
        elif choice=='2':
            file_name=input('Введите имя файла: ')
            handler_planets.save_to_file(file_name)
            saved=True
        elif choice=='3':
            if not(handler_planets.planets):
                print('⛔БД пустая')
            else:
                for planet in handler_planets.planets:
                    print(planet)
        elif choice=='4':
            saved=False
            handler_planets.add_planet()
        elif choice=='5':
            handler_planets.search()
        elif choice=='6':
            saved=False
            handler_planets.edit_planet()
        elif choice=='7':
            saved=False
            handler_planets.delete_planet()
        elif choice=='8':
            saved=False
            handler_planets.sort_planets()
        elif choice=='9':
            handler_planets.export_to_csv()
        elif choice=='10':
            if saved:
                handler_planets.exit()
                break
            else:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n❗ Вы не сохранили текущие изменения. При выходе они будут утеряны. Вы уверены, что хотите завершить работу программы?')
                choice=input('Выбор(да/нет): ')
                if choice.lower()=='да':
                    handler_planets.exit()
                    break
        elif choice=='11':
            handler_planets.settings()

        else:
            print('❌ Неверный выбор!')