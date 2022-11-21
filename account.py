class Account:
    """
    Class representing a bank account
    """

    def __init__(self, name: str) -> None:
        """
        Initializes account name and balance
        :param name: Account name (i.e. John, Catherine, etc.)
        """
        self.__account_name = name  # 'Name'
        self.__account_balance = 0  # 0.00

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit money into account
        :param amount: amount of money to be deposited
        :return: returns if transaction was successful
        """
        try:
            self.__account_balance += amount  # 0.00 + amount in form of #.##

            if self.__account_balance > 0:
                return True
            else:
                self.__account_balance = 0
                return False

        except TypeError:
            print('Enter a valid whole or decimal number')
            return False

        except ValueError:
            print('Enter a valid number greater than zero')
            return False

        except:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw money from account
        :param amount: amount of money to be withdrawn
        :return: returns if transaction was successful
        """
        try:
            if amount > 0:
                if self.__account_balance >= amount:
                    self.__account_balance -= amount  # 0.00 + amount in form of #.##
                    return True
                else:
                    self.__account_balance = 0
                    return False
            else:
                return False

        except TypeError:
            print('Enter a valid whole or decimal number')
            return False

        except ValueError:
            print('Enter a valid number greater than zero and less than or equal to your balance')
            return False

    def get_balance(self) -> float:
        """
        Gets current account balance
        :return: returns balance
        """
        return self.__account_balance  # number in form of #.##

    def get_name(self) -> str:
        """
        Gets current account name
        :return: returns name
        """
        return self.__account_name  # 'Name'
