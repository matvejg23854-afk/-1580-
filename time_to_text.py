def time_to_text(hour,minute):
    #Проверка на особые случаи, кроме "минуты 00"
    if hour == 0 and minute == 0:
        return "полночь"
    elif hour == 12 and minute == 0:
        return "полдень"
     #Если нет особых случаев, программа идет переводить часы, затем минуты. Т.к. текст будет вывода будет "склеиваться", введем новую переменную result
     
     #
     #Справка:
     #1,21, - час
     #2-4,22,23 - часа
     #Остальное - часов
     #1,21,31,41,51 - минута
     #2-4,22-24,32-34,42-44,52,54 - минуты
     #Остальное - минут
     
     
    result=str()
    no_minutes=False #Флаг для особого случая с "ровно"
    if hour>=13:
        hour_form=hour-12
    else:
        hour_form=hour
        
        
    #Часы    
    if hour_form==1 or hour_form==21:
        result=result+str(hour_form)+' час '
    elif hour_form>=2 and hour_form<=4 or hour_form==22 or hour_form==23:
        result=result+str(hour_form)+' часа '
    else:
        result=result+str(hour_form)+' часов '
        
        
    #Минуты
    #minute_remainder=minute%10 не оимеет смысла делать,т.к.
    if minute==1 or minute==21 or minute==31 or minute==41 or minute==51:
        result=result+str(minute)+' минута '
    elif minute>=2 and minute<=4 or minute>=22 and minute<=24 or minute>=32 and minute<=34 or minute>=42 and minute<=44 or minute>=52 and minute<=54:
        result=result+str(minute)+' минуты '
        
    #Проверка особого случая
    elif minute==0:
        no_minutes=True     
    else:
        result=result+str(minute)+' минут '
    
    #Обработка времнных интервалов
    if hour<6:
        result+='ночи'
    elif hour<12:
        result+='утра'
    elif hour<18:
        result+='дня'
    elif hour<24:
        result+='вечера'
        
    if no_minutes:
        result+=' ровно'
    
    return result     
  
         
     
         
     

def check_time_input(time):
    
    if len(time)==0:
        return "Введены недопустимые данные: вы ничего не ввели", False
    elif len(time)<2 or len(time)>2:
        return "Введены недопустимые данные: вы неправильно ввели данные. Формат: час минута", False
    
    
    try:
        hour,minute =time[0],time[1]
        if time[0]=='-0':
            return "Введены недопустимые данные: часы должны быть от 0 до 23.", False
        elif time[1]=='-0':
            return "Введены недопустимые данные: минуты должны быть от 0 до 59", False
        hour,minute=int(time[0]),int(time[1])
        if hour>23 or hour<0:
            return "Введены недопустимые данные: часы должны быть от 0 до 23.", False
        elif minute>59 or minute<0:
            return "Введены недопустимые данные: минуты должны быть от 0 до 59", False
        
    except ValueError:
        return "Введены недопустимые данные: программа принимает только натуральные числа и 0", False
    
    else:
        return "",True
    
def main():    
    time_input=input("Введите час и минуту: ").split()
    
    error_message,is_valid=check_time_input(time_input)
    
    if not is_valid:
        print(error_message)
        
    else:
        print(time_to_text(int(time_input[0]),int(time_input[1])))
        
    pass

if __name__ == "__main__":
    main()


