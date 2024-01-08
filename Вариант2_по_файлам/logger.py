from date_create import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{adress}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt','a', encoding='UTF-8') as file:
        file.write(contact)

def show_info():
    with open('phonebook.txt','r', encoding='UTF-8') as file:
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

    with open('phonebook.txt','r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
           
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n',' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)