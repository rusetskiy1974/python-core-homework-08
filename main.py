from datetime import date, datetime
 

def get_birthdays_per_week(users):
    
    WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"]

    user_list_including_birthday = {} 
                           # Створюємо словник для зберігання імен 
    current_datetime = date.today() 
    # current_datetime = datetime(2023, 12, 29).date()   
    print (current_datetime.year)
     
    if not users:                                            # Перевірка на порожній список 
        return {}
    
    for volume in users:                                     # Циклічно переглядаємо вхідні дані зі словника users
                                
        # birthday_current_year = datetime(current_datetime.year, volume['birthday'].month, 
                                                        #   volume['birthday'].day).date() 
        birthday_current_year = volume['birthday'].replace(year = current_datetime.year)
        
        # birthday_current_year = birthday_current_year.replace(year = current_datetime.year)
        
                                                             # Визначаємо дату народження в поточному році
        
        if birthday_current_year < current_datetime < datetime(current_datetime.year, 12, 26).date():
            continue                                         # Перевірка умови, коли день народження вже минув у цьому році
        
        elif birthday_current_year == current_datetime:  
                key_entry_check_week = 0                     # Визначення ключа входження дати народження
                                                             # в поточний тиждень

        elif birthday_current_year > current_datetime:       # Визначення днів народження  що є у майбутньому
                # key_entry_check_week = int(str(birthday_current_year - current_datetime).split()[0]) 
                key_entry_check_week = (birthday_current_year - current_datetime).days
                # print (key_entry_check_week, '------', key_www)
                                                             # Визначення коли деякі дня народження вже минули у цьому році..
        else:                                                # але будуть на наступному тижні
                # key_entry_check_week = int(str(datetime(current_datetime.year, 12, 31).date() \
                                                        # - current_datetime).split()[0]) \
                                                        #   + birthday_current_year.day
                key_entry_check_week = (datetime(current_datetime.year, 12, 31).date() - current_datetime).days + birthday_current_year.day
                birthday_current_year = (birthday_current_year.replace(year = current_datetime.year+1))
                print (key_entry_check_week,'-----', birthday_current_year)
                # birthday_current_year = datetime(current_datetime.year+1, volume['birthday'].month, \
                                        # volume['birthday'].day).date()
            
         
        if 0 <= key_entry_check_week < 7:                    # Перевірка входження дати народження в тижневий інтервал
                        
            day_week =  birthday_current_year.strftime('%A') # Визначення дня тижня в день народження 
             

            if day_week in ["Saturday", "Sunday"] and current_datetime.weekday() > 0:
                day_week = "Monday"                          # Визначення вихідних днів  і перенесення  їх на понеділок  

            if day_week in user_list_including_birthday:     # Запис імен в список словника
                user_list_including_birthday[day_week].append(volume['name'].split()[0])
            else:
                user_list_including_birthday[day_week] = [volume['name'].split()[0]]   
             
    sort_result_dikt = {}                                    # Сортування вихідного словника
    for day in WEEK_DAYS:
        for volume in user_list_including_birthday.keys():
            if day == volume:
                sort_result_dikt[day] = user_list_including_birthday[volume]

         
    return  sort_result_dikt 

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2000, 12, 29).date()},
        {"name": "Ban Reum", "birthday": datetime(2000, 12, 30).date()},
        {"name": "San Reum", "birthday": datetime(2006, 12, 31).date()},
        {"name": "Fan Reum", "birthday": datetime(2015, 1, 1).date()},
        {"name": "kan Reum", "birthday": datetime(2000, 1, 2).date()},
        {"name": "Wan Reum", "birthday": datetime(2000, 1, 3).date()}
    ]

    sort_result_dikt = get_birthdays_per_week(users)
    print(sort_result_dikt)
    # Виводимо результат
    for day_name, names in sort_result_dikt.items():
        print(f"{day_name}: {', '.join(names)}")
