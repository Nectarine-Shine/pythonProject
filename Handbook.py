from PersInfo import PersInfo

class Handbook:

    def __init__(self, name):
        self.name = name

    def add_info(self):
        print('Введите через пробел имя, фамилию, номер телефона, город и e-mail: ', end='\n')
        newInfo = PersInfo(input())
        if newInfo.confirm():
            handbook = open(self.name + '.txt', 'r')
            informations = handbook.read()
            handbook.close()
            if newInfo.write_in_one_line() in informations:
                print('Такая запись уже существует.', end='\n')
                return
            if newInfo.email in informations:
                print('Запись с таким e-mail уже существует.', end='\n')
                return
            handbook = open(self.name + '.txt', 'a')
            handbook.write(newInfo.write_in_one_line() + '\n')
            handbook.close()
            print('Запись добавлена.', end='\n')
        else:
            print('Неверный ввод. Повторите попытку.')

    def change_info(self):
        print('Введите e-mail изменяемой записи:', end='\n')
        email = input()
        handbook = open(self.name + '.txt', 'r')
        informations = handbook.read()
        handbook.seek(0)
        if '@' not in email:
            print('Неверный ввод. Повторите попытку.', end='\n')
            return
        if email in informations:
            print('Введите новое значение:', end='\n')
            changedInfo = PersInfo(input())
            if changedInfo.confirm():
                informations = handbook.readlines()
                handbook.close()
                handbook = open(self.name + '.txt', 'w')
                for info in informations:
                    if email in info:
                        handbook.write(changedInfo.write_in_one_line() + '\n')
                    else:
                        handbook.write(info + '\n')
                print('Значение изменено.', end='\n')
            else:
                print('Неверный ввод. Повторите попытку.', end='\n')
            return
        print('Такой записи не существует.', end='\n')

    def find_info(self):
        print('Введите один из параметров для поиска:', end='\n')
        searchingParam = input()
        foundInformationsCount = 0
        handbook = open(self.name + '.txt', 'r')
        informations = handbook.readlines()
        for info in informations:
            if searchingParam in info:
                print(info)
                foundInformationsCount += 1
        handbook.close()
        print('Найдено записей: ', foundInformationsCount, end='\n')

    def delete_info(self):
        print('Введите e-mail удаляемой записи:', end='\n')
        email = input()
        handbook = open(self.name + '.txt', 'r')
        informations = handbook.readlines()
        handbook.close()
        handbook = open(self.name + '.txt', 'w')
        isDeleted = False
        for info in informations:
            if email not in info:
                handbook.write(info)
            else:
                isDeleted = True
        handbook.close()
        if isDeleted:
            print('Запись удалена.', end='\n')
        else:
            print('Записи с таким e-mail не существует.', end='\n')
