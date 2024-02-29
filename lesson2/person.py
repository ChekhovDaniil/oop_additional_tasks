"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self) -> None:
        """Выводит на экран имя и возраст человека."""
        print(f'{self.name} is {self.age} years old.')

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """
        :param name: Имя человека
        :param birth_year: Возраст человека
        :return: Объект класса Person
        """
        return cls(name, 2024 - birth_year)

    @staticmethod
    def is_adult(age) -> bool:
        """
        Возвращает True если возраст человека больше 18 и False в противном случае.
        :param age: Возраст человека
        :return: bool
        """
        if age >= 18:
            return True
        return False


# код для проверки
person1 = Person("John", 28)
person1.display()  # John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
person2.display()  # Mike is 26 years old

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
