"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amount) -> None:
        """Вносит деньги на счёт."""
        self.balance += amount

    def withdraw(self, amount) -> None:
        """Снимает деньги со счёта."""
        self.balance -= amount

    def close(self) -> int:
        """Закрывает счёт и возвращает оставшиеся на нём деньги."""
        self.balance = 0
        return self.balance


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
