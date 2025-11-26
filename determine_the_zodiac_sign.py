
def check_date_input(date):
    
    if len(date)==0:
        return "Введены недопустимые данные: вы ничего не ввели", False
    elif len(time)<2 or len(time)>2:
        return "Введены недопустимые данные: вы неправильно ввели данные. Формат: ЧИСЛО МЕСЯЦ", False
    
    
    try:
        day,mounth =date[0],date[1]
        if date[0]=='-0':
            return "Введены недопустимые данные: день должен быть от 0", False
        elif date[1]=='-0':
            return "Введены недопустимые данные: месяц должен быть от 0", False
        day,mounth=int(time[0]),int(time[1])
        if mounth>12 or mounth<0:
            return "Введены недопустимые данные: месяц должны быть от 0 до 12", False
        
        
        #проверка дней по месяцам:
        '''
        Справка
        Январь (1) - 31
        Февраль (2) - 29
        Март (3) - 31
        Апрель (4) - 30
        Май (5) - 31
        Июнь (6) - 30
        Июль (7) - 31
        Август (8) - 31
        Сентябрь (9) - 30
        Октябрь (10) - 31
        Ноябрь (11) - 30
        Декабрь (12) - 31
        '''
        if mounth==2:
            pass
        
    except ValueError:
        return "Введены недопустимые данные: программа принимает только натуральные числа и 0", False
    
    else:
        return "",True

def main():    
    date_input=input("Введите дату в формате: ЧИСЛО МЕСЯЦ").split()
    
    error_message,is_valid=check_time_input(date_input)
    
    if not is_valid:
        print(error_message)
        
    else:
        pass

if __name__ == "__main__":
    main()