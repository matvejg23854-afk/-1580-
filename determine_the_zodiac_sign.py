import time


def determine_the_zodiac_sign(date):
    result="Знак зодиака вашей даты: "
    
    day,mounth =int(date[0]),int(date[1])
    
    #ВОДОЛЕЙ
    if ( mounth==1 and day>20 ) or (  mounth==2 and day<20 ):
        result+='Водолей'
    #РЫБЫ
    elif ( mounth==2 and day>19 ) or (  mounth==3 and day<21 ):
        result+='Рыбы'
    #ОВЕН
    elif ( mounth==3 and day>20 ) or (  mounth==4 and day<21 ):
        result+='Овен'
    #ТЕЛЕЦ
    elif ( mounth==4 and day>20 ) or (  mounth==5 and day<22 ):
        result+='Телец'
    #БЛИЗНЕЦЫ
    elif ( mounth==5 and day>21 ) or (  mounth==6 and day<22 ):
        result+='Близнецы'
    #РАК
    elif ( mounth==6 and day>21 ) or (  mounth==7 and day<23 ):
        result+='Рак'
    #ЛЕВ
    elif ( mounth==7 and day>22 ) or (  mounth==8 and day<22 ):
        result+='Лев'
    #ДЕВА
    elif ( mounth==8 and day>21 ) or (  mounth==9 and day<24 ):
        result+='Дева'
    #ВЕСЫ
    elif ( mounth==9 and day>23 ) or (  mounth==10 and day<24 ):
        result+='Весы'
    #СКОРПИОН
    elif ( mounth==10 and day>23 ) or (  mounth==11 and day<23 ):
        result+='Скорпион'
    #СТРЕЛЕЦ
    elif ( mounth==11 and day>22 ) or (  mounth==12 and day<23 ):
        result+='Стрелец'
    #КОЗЕРОГ
    elif ( mounth==12 and day>22 ) or (  mounth==1 and day<21 ):
        result+='Козерог'    
    
    
    

    
    return result
        
    
    
def check_date_input(date):
    
    if len(date)==0:
        return "Введены недопустимые данные: вы ничего не ввели", False
    elif len(date)<2 or len(date)>2:
        return "Введены недопустимые данные: вы неправильно ввели данные. Формат: ЧИСЛО МЕСЯЦ", False
    
    
    try:
        day,mounth =int(date[0]),int(date[1])
    
        if day<1:
            return "Введены недопустимые данные: день должен быть от 1", False
        if mounth>12 or mounth<1:
            return "Введены недопустимые данные: месяц должен быть от 1 до 12", False
       
        
        
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
        mountheswith30days=[4,6,9,11]
        if mounth==2:
            if day>29:
                return "Введены недопустимые данные: в этом месяце может не может быть больше 29 дней", False
        elif mounth in mountheswith30days:
            if day>30:
                return "Введены недопустимые данные: в этом месяце может не может быть больше 30 дней", False
        else:
            if day>31:
                return "Введены недопустимые данные: в этом месяце может не может быть больше 31 дня", False
        
    except ValueError:
        return "Введены недопустимые данные: программа принимает только натуральные числа и 0", False
    
    else:
        return "",True

def main():
    print("Привет! Это программа для определения знака зодиака")
    time.sleep(1)
    
    date_input=input("Введите дату: ").split()
    
    error_message,is_valid=check_date_input(date_input)
    
    if not is_valid:
        print(error_message)
        
    else:
        print(determine_the_zodiac_sign(date_input))
        
if __name__ == "__main__":
    main()
