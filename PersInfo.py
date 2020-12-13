class PersInfo:

    def __init__(self, row):
        info = row.split(' ')
        self.fieldsCount = len(info)
        self.firstName = info[0]
        self.lastName = info[1]
        self.phoneNumber = info[2]
        self.city = info[3]
        self.email = info[4]

    def confirm(self):
        if self.fieldsCount != 5:
            return False
        isFirstNameCorrect = all(map(str.isalpha, self.firstName)) and self.firstName[0].isupper()
        isLastNameCorrect = all(map(str.isalpha, self.lastName)) and self.lastName[0].isupper()
        isPhoneNumberCorrect = all(map(str.isdigit, self.phoneNumber)) and self.phoneNumber[0] == '8' and len(
            self.phoneNumber) == 11
        isCityCorrect = all(map(str.isalpha, self.city)) and self.city[0].isupper()
        isEmailCorrect = '@' in self.email
        return isFirstNameCorrect and isLastNameCorrect and isPhoneNumberCorrect and isCityCorrect and isEmailCorrect

    def write_in_one_line(self):
        return '{} {} {} {} {}'.format(self.firstName, self.lastName, self.phoneNumber, self.city, self.email)