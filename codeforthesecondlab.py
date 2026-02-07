from prettytable import PrettyTable
import random

def check_data(value=None,check_type=None):
    if check_type=='mode':
        return value in ('0','1','2')
    if check_type=='change':
        return value in ('1','2')
    if check_type=='array':
        arr=value
        if not isinstance(arr,list) or len(arr)==0:
            print("Ошибка: массив пуст")
            return False
        wrong=[i for i,x in enumerate(arr) if not isinstance(x,int)]
        if wrong:
            print(f"Ошибка: некорректные элементы массива {wrong}")
            return False
        return True

def bubble_sort(arr):
    comparisons=0
    swaps=0
    sorted_flag=False
    n=len(arr)
    while not sorted_flag:
        sorted_flag=True
        for i in range(n-1):
            comparisons+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swaps+=1
                sorted_flag=False
    return arr,comparisons,swaps

def selection_sort(arr):
    comparisons=0
    swaps=0
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            comparisons+=1
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        swaps+=1
    return arr,comparisons,swaps

def quick_sort(arr):
    comparisons=0
    swaps=0
    def _quick_sort(a):
        nonlocal comparisons,swaps
        if len(a)<=1:
            return a
        pivot=a[0]
        left=[]
        right=[]
        for x in a[1:]:
            comparisons+=1
            if x<pivot:
                left.append(x)
                swaps+=1
            else:
                right.append(x)
                swaps+=1
        return _quick_sort(left)+[pivot]+_quick_sort(right)
    sorted_arr=_quick_sort(arr)
    return sorted_arr,comparisons,swaps

def change_array(arr):
    while True:
        choice=input("Изменить весь массив(1) или часть массива(2)?")
        if not check_data(choice,'change'):
            print("Ошибка выбора режима изменения")
            continue
        if choice=='1':
            new_arr=input("Введите новый массив через пробел:")
            try:
                arr=[int(x) for x in new_arr.split()]
            except ValueError:
                print("Данные некорректны.Массив должен быть из целых чисел.")
                continue
        else:
            try:
                index=int(input(f"Введите индекс элемента(0-{len(arr)-1}):"))
                new_value=input("Введите новое значение элемента:")
                arr[index]=int(new_value)
            except(ValueError,IndexError):
                print("Данные некорректны.Целое число и корректный индекс.")
                continue
        repeat=input("Изменить ещё раз?(да/нет):").lower()
        if repeat!='да':
            break
    return arr

def print_table(arr,bubble,selection,quick):
    table=PrettyTable()
    table.field_names=["Сортировка","Массив","Сравнения","Перестановки"]
    table.add_row(["Пузырьком",bubble[0],bubble[1],bubble[2]])
    table.add_row(["Выбором",selection[0],selection[1],selection[2]])
    table.add_row(["Хоара",quick[0],quick[1],quick[2]])
    print("\nИсходный массив:",arr)
    print(table)

def demo_mode():
    while True:
        arr=[random.randint(0,99) for _ in range(10)]
        b_arr=bubble_sort(arr.copy())
        s_arr=selection_sort(arr.copy())
        q_arr=quick_sort(arr.copy())
        print_table(arr,b_arr,s_arr,q_arr)
        repeat=input("Отсортировать ещё раз?(да/нет):").lower()
        if repeat!='да':
            break

def interactive_mode():
    while True:
        try:
            size=int(input("Введите размер массива:"))
            if size<=0:
                print("Размер должен быть больше 0")
                continue
        except ValueError:
            print("Размер должен быть целым числом")
            continue

        arr_input=input(f"Введите {size} элементов через пробел:")
        try:
            arr=[int(x) for x in arr_input.split()]
        except ValueError:
            print("Данные некорректны.Массив должен содержать целые числа")
            continue

        if len(arr)!=size:
            print(f"Количество элементов не совпадает с размером({size})")
            continue

        print(f"Вы ввели массив:{arr}")
        confirm=input("Подтверждаете?(да/нет):").lower()
        if confirm!='да':
            continue

        if not check_data(arr,'array'):
            continue

        modify=input("Хотите изменить массив?(да/нет):").lower()
        if modify=='да':
            arr=change_array(arr)
            if not check_data(arr,'array'):
                continue

        b_arr=bubble_sort(arr.copy())
        s_arr=selection_sort(arr.copy())
        q_arr=quick_sort(arr.copy())
        print_table(arr,b_arr,s_arr,q_arr)

        repeat=input("Отсортировать ещё раз?(да/нет):").lower()
        if repeat!='да':
            break

def main():
    print("Доступные сортировки:Пузырьком,Выбором,Хоара")
    print("Режимы:1-Демонстративный,2-Интерактивный,0-Выход")
    while True:
        mode = input("Выберите режим:")
        if not check_data(mode, 'mode'):
            print("Ошибка выбора режима.Пример:1")
            continue
        if mode == '0':
            break
        elif mode == '1':
            demo_mode()
        elif mode == '2':
            interactive_mode()

if __name__ == "__main__":
    main()