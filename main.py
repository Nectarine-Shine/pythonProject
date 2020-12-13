import os.path
from Handbook import Handbook


def main():
    result = 0
    while True:
        result = select_action()
        if result == -1:
            break


def select_action():
    print("Список действий:", end = '\n')
    print("Создать справочник - нажмите 1", end = '\n')
    print("Выбрать справочник - нажмите 2", end = '\n')
    print("Показать имеющиеся справочники - нажмите 3", end='\n')
    print("Добавить запись - нажмите 4", end='\n')
    print("Изменить запись - нажмите 5", end='\n')
    print("Найти запись - нажмите 6", end='\n')
    print("Удалить запись - нажмите 7", end='\n')
    print("Завершить работу - нажмите 0", end='\n')
    number = int(input())
    if number == 1:
        create_handbook()
    elif number == 2:
        select_handbook()
    elif number == 3:
        view_handbooks()
    elif number == 4:
        currentHandbook.add_info()
    elif number == 5:
        currentHandbook.change_info()
    elif number == 6:
        currentHandbook.find_info()
    elif number == 7:
        currentHandbook.delete_info()
    elif number == 0:
        return -1
    return 1


def create_handbook():
    global currentHandbook
    hanbookName = input("Введи название справочника: ")
    if os.path.exists(os.path.abspath(hanbookName + '.txt')):
        print('Справочник с таким именем уже существует.', end='\n')
        return
    currentHandbook = Handbook(hanbookName)
    handBooks[hanbookName] = currentHandbook
    handbook = open(hanbookName + '.txt', 'a')
    handbook.close()
    print('Справочник создан.', end='\n')


def select_handbook():
    global currentHandbook
    handbookName = input("Введите имя нужного справочника: ")
    if os.path.exists(os.path.abspath(handbookName + '.txt')):
        currentHandbook = handBooks[handbookName]
        print('Текущий справочник изменён на ', handbookName, '.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (yes/no)', end='\n')
        answer = input()
        if answer == 'yes':
            currentHandbook = Handbook(handbookName)
            handBooks[handbookName] = currentHandbook
            handbook = open(handbookName + ".txt", "a")
            handbook.close()
            print('Справочник создан.', end='\n')
        if answer == 'no':
            return


def view_handbooks():
    for key in handBooks.keys():
        print(key, end='\n')


handBooks = dict()
currentHandbook = Handbook('')
handBooks[''] = currentHandbook

for file in os.listdir(os.getcwd()):
    if file.endswith('.txt'):
        handBooks[file[:-4]] = Handbook(file[:-4])
main()