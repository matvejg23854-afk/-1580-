planets=[]
deleted_planets=[]
from planet import Planet
def input_float(text):
    while True:
        try:
            value=float(input(text))
            if value<=0:
                print("❌ Значение должно быть больше 0")
                continue
            return value
        except ValueError:
            print("❌ Введите число!")
def input_str(text):
    while True:
        value=input(text).strip()
        if value:
            return value
        print("❌ Текстовое значение не может быть пустым")

def load_from_file(file_name):
    if planets:
        print('❗ При открытии файла текущие изменения будут утеряны. Вы уверены, что хотите открыть файл?')
        choice = input('Выбор(да/нет): ')
        if choice.lower() == 'да':
            pass
        else:
            return
    deleted_planets.extend(planets)
    planets.clear()
    while True:
        try:
            with open(file_name,'r',encoding='UTF-8') as file_r:
                for string in file_r:
                    if not string.strip():
                        continue

                    data=string.strip().split(';')
                    planet=Planet(data[0],
                                  float(data[1]),float(data[2]),float(data[3]), #прикольно, кстати, но в book я исправил баг с чтением строки, а тут нет. Если успею исправить, то круто
                                  data[4])
                    planets.append(planet)
                print('✅ Планеты успешно загружены!')
                return
        except FileNotFoundError:
            print('❌ Файл не найден')
            return

def save_to_file(file_name):
    with open(file_name,'w',encoding='UTF-8') as file_w:
        for planet in planets:
            file_w.write(f'{planet.name};{planet.radius};{planet.mass};{planet.distance};{planet.planet_type}\n')
        print(f'✅ Планеты успешно сохранены!')

def add_planet():
    name=input_str('Введите название планеты: ')
    radius = input_float('Введите радиус планеты (в км): ')
    mass = input_float('Введите массу планеты (в кг): ')
    distance = input_float('Введите расстояние от планеты до Солнца (в км): ')
    planet_type = input_str('Введите тип планеты: ')

    planet=Planet(name,radius,mass,distance,planet_type)
    planets.append(planet)
    print(f'✅ Планета {planet.name} с ID {planet.id} успешно создана!')

def delete_planet():
    print('~~~~~~~~~~~~МЕНЮ УДАЛЕНИЯ~~~~~~~~~~~~')
    print('1 - удаление по названию планеты')
    print('2 - удаление по ID планеты')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    choice = input('Выбор: ')
    if choice=='1':
        name=input('Введите название планеты для удаления: ')
    elif choice=='2':
        id=input('Введите ID планеты для удаления: ')
    else:
        print("❌ Неверный выбор")
        return

    key=False
    copy_planets=planets.copy()
    for planet in copy_planets:
        if choice=='1':
            if planet.name.lower() == name.lower():
                deleted_planets.append(planet)
                planets.remove(planet)
                key=True


        elif choice=='2':
            if str(planet.id) == id:
                deleted_planets.append(planet)
                planets.remove(planet)
                print("✅ Планета успешно удалена")
                return
    if key:
        print(f"✅ Планет(а/ы) с названием: {name} успешно удален(а/ы)")
        return

    print("❌ Планета для удаления не найдена")
def edit_planet():
    id=input('Введите ID планеты для изменения параметров: ')

    for planet in planets:
        if str(planet.id)==id:
            print('Введите новые данные планеты')
            print()
            planet.name=input_str('Название: ')
            planet.radius=input_float('Радиус (в км):')
            planet.mass=input_float('Масса (в кг):')
            planet.distance=input_float('Расстояние от планеты до Солнца (в км):')
            planet.planet_type=input_str('Тип: ')
            print()
            print('✅ Планета успешно изменена')
            return
    print("❌ Планета не найдена")

def search():
    print('~~~~~~~~~~~~МЕНЮ ПОИСКА~~~~~~~~~~~~')
    print('1 - поиск по названию планеты')
    print('2 - поиск по типу планеты')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    choice=input('Выбор: ')
    found=False

    if choice=='1':
        name=input('Введите название планеты: ')

        for planet in planets:
            if planet.name.lower()==name.lower():
                print(planet)
                found=True

    elif choice=='2':
        planet_type=input('Введите тип планеты: ')

        for planet in planets:
            if planet.planet_type.lower()==planet_type.lower():
                print(planet)
                found=True
    else:
        print("❌ Неверный выбор")
        return
    if not found:
        print('⛔ Ничего не найдено')
def sort_planets():
    if not planets:
        print("⛔ БД пустая")
        return
    print("~~~~~~~~~~~~СОРТИРОВКА~~~~~~~~~~~~")
    print("1 - по расстоянию до Солнца")
    print("2 - по радиусу")
    print("3 - по массе")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice = input("Выбор: ")
    n = len(planets)
    for i in range(n):
        for j in range(n - i - 1):
            if choice=='1':
                condition=planets[j] > planets[j + 1]
            elif choice=='2':
                condition = planets[j].radius>planets[j + 1].radius
            elif choice=='3':
                condition=planets[j].mass>planets[j + 1].mass

            else:
                print("❌ Неверный выбор")
                return

            if condition:
                planets[j], planets[j + 1] = planets[j + 1], planets[j]

    print("✅ Планеты успешно отсортированы")

def export_to_csv():
    print('❗ ВНИМАНИЕ!\n1)Формат .csv сохраняет данные без учета форматирования.\n2)Если файл с данным названием существует, то он должен быть закрыт.')

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

        file_w.write("name\tradius\tmass\tdistance\tplanet_type\n")

        for planet in planets:
            file_w.write(f"{planet.name}\t{planet.radius}\t{planet.mass}\t{planet.distance}\t{planet.planet_type}\n")

    print("✅ Экспорт в CSV завершён")
def exit():
    print('✅ Успешный выход!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def settings():
    print('~~~~~~~~~~~~НАСТРОЙКИ~~~~~~~~~~~~')
    print('1 - просмотр удаленных планет')
    print('2 - назад')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    choice=input('Выбор: ')
    if choice=='1':
        if not(deleted_planets):
            print('❌ Нет удаленных планет!')
        for del_planet in deleted_planets:
            print(del_planet)
    elif choice=='2':
        pass
    else:
        print('❌ Неверный выбор!')
        return settings()