# Создать телефонный справочник с возможностью импорта и экспорта данных 
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1) Создать телефонный справочник:
#  - Открыть файл в режиме добавления (а)
# 2) Добавить контакт:
#  - Запросить информацию у пользователя
#  - Подготовить данные в необходимом формате
#  - Открыть файл в режиме добавления (а)
#  - Добавить контакт в файл
# 3) Вывести данные из файла на экран:
#  - ОТкрыть файл в режиме чтения (r)
#  - Вывести данные на экран
#  4) Поиск данных:
#  - Запросить вариант поиска
#  - Запросить данные поиска
#  - ОТкрыть файл в режиме чтения (r)
#  - Сохранить переменную
#  - Вывести нужную информацию на экран
# 5) Реализовать UI (User Interface):
#  - Вывести варианты меню
#  - Получение запроса пользователя
#  - Реализация запроса пользователя
#  - Выход из программы

def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{adress}\n\n'

def add_contact():
    contact = create_contact()
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt','a', encoding='UTF-8') as file:
        file.write(contact)

def show_info():
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt','r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(*enumerate(contacts_list,1))
        for contact in enumerate(contacts_list,1):
            print(*contact)
        # print(file.read().rstrip())

def search_contact():
    print(
        'Выберите вариант поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: ')                 
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод данных')
            var_search = input('Выберите вариант поиска: ')

    index_var = int(var_search)-1

    search = input('ВВедите данные для поиска: ')

    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt','r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
           
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n',' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)

def copy_contact():
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt','r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list,1):
            print(*contact)
        number_contact = int(input('Введите номер контакта для копирования: '))
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/new_phonebook.txt','a', encoding='UTF-8') as file:
        file.writelines(f'{contacts_list[number_contact-1]}\n\n')

def delete_contact():
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt',
              'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list,1):
            print(*contact)
        number_contact = int(input('Введите номер контакта для удаления: '))
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt',
              'w', encoding='UTF-8') as file:
        for i in range(number_contact-1):
            file.write(f'{contacts_list[i]}\n\n')
        for i in range(number_contact, len(contacts_list)):
            file.write(f'{contacts_list[i]}\n\n')

def interface():
    with open('c:/Users/sko88/OneDrive/Рабочий стол/GB/SPEC/01 Python/Seminar8/phonebook1.txt','a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '6':
        print('Варианты меню: \n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Скопировать контакт в файл\n'
            '5. Удалить контакт\n'
            '6. Выход из программы')
        command = input('Выберите пункт меню: ')
    
        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод данных')
            command = input('Выберите пункт меню: ')

        match command:
            case '1':
                add_contact()
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_contact()    
            case '5':
                delete_contact() 
            case '6':
                print("Всего хорошего!")       

interface()