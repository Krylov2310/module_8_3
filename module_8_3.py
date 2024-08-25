print('\033[30m\033[47mДомашнее задание по теме "Создание исключений".\033[0m')
print('\033[30m\033[47mЗадача "Некорректность":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        if self.__is_valid_vin(__vin):
            self.__vin = int(__vin)
        if self.__is_valid_numbers(__numbers):
            self.__numbers = str(__numbers)

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# Пример выполняемого кода:
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
print()
print(thanks)
