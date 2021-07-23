from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def output_name():
    """
    Выводит имя по номеру документа
    """
    count = 0
    while True:
        number_document = input("Введите номер документа:")
        for i in documents:
            if i['number'] == number_document:
                print(i["name"], '\n')
                count=1
        if count == 1:
            break
        else:
            print('Номер документа не найден, повторите ввод ')

def out_directories():
    """
        Выводит номер полки на котором находится документ
    """
    count = 0
    while True:
        number_document = input("Введите номер документа:")
        for key, value in directories.items():
            if number_document in value:
                print(f'Документ находится на {key} полке', '\n')
                count = 1
        if count == 1:
            break
        else:
            print('Номер документа не найден, повторите ввод ')

def output_list_document():
    """
        Выводит список всех документов
    """
    for i in documents:
        for key, value in i.items():
            print(value, end=' ')
        print()
    print()

def add_document():
    """
        Добавляет новый документ
    """
    while True:
        type= input('Введите тип документа: ')
        if type == '':
            print('Некоректный ввод')
        else:
            break
    while True:
        number = input('Введите номер документа: ')
        if number == '':
            print('Некоректный ввод')
        else:
            break
    while True:
        name= input('Введите фамилию и имя: ')
        if name == '':
            print('Некоректный ввод')
        else:
            break
    new_document = {"type": type, "number": number, "name": name}
    while True:
        directories_document = input('Введите номер полки: ')
        if directories_document not in directories:
            print('Такой полки не существует, повторите ввод ')
        else:
            break
    return new_document, directories_document

def del_document():
    """
        Удаляет документ из каталога
    """
    count = 0
    while True:
        number_document = input("Введите номер документа:")
        for i in documents:
            for key, value in i.items():
                if number_document == value:
                    documents.remove(i)
                    for directorie, numbers in directories.items():
                        for j in numbers:
                            if j == number_document:
                                numbers.remove(j)
                    print(f' Документ удален')
                    count = 1
        if count == 1:
            break
        else:
            print('Номер документа не найден, повторите ввод ')
    print(directories)
    print()

def move_document():
    """
        Перемещает документ на указанную полку
    """
    count = 0
    while True:
        number_document = input("Введите номер документа, который хотите переместить:")
        number_dirictories = input("Введите номер целевой полки:")
        for directorie, numbers in directories.items():
                for j in numbers:
                    if j == number_document:
                        numbers.remove(j)
                        count = 1
                        for directorie, numbers in directories.items():
                             if  number_dirictories == directorie:
                                 numbers.append(number_document)
                                 count += 1
        if count == 2:
            print(f'Докумен {number_document} перемещен на {number_dirictories} полку')
            break
        else:
            print('Номер документа или целевой полки  введен неверно, повторите ввод ')
    print(directories)

def add_shelf():
    """
        Добавляет новую полку
    """
    while True:
        directorie = input('Введите номер полки, которую хотите добавить: ')
        if directorie  in directories:
            print('Такая полка  существует, повторите ввод ')
        else:
            directories[directorie] = []
            break
    print(directories, '\n')
def main():
     while True:
         user_input = input(
"""people - p 
shelf - s 
list - l, 
add - a 
delete - d
move - m
add shelf - as
quit - q 
Выбирите команду: """)
         if user_input == 'p':
             output_name()
         elif user_input == 's':
             out_directories()
         elif user_input == 'l':
             output_list_document()
         elif user_input == 'a':
            new_doc, director_doc = add_document()
            documents.append(new_doc)
            directories[director_doc].append(new_doc['number'])
            print('Документ успешно добавлен')
            pprint(documents)
            pprint(directories)
            print()
         elif user_input == 'd':
             del_document()
         elif user_input == 'm':
             move_document()
         elif user_input == 'as':
             add_shelf()
         elif user_input == 'q':
             print('Программа завершена')
             break
         else:
             print('Команда введена неверно')

main()