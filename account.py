class Account:
    """
    Class representing a bank account
    """

    def __init__(self, name):
        """
        Initializes account name and balance
        :param name: Account name (i.e. John, Catherine, etc.)
        """
        self.account_name = name  # 'Name'
        self.account_balance = 0  # 0.00

    def deposit(self, amount):
        """
        Function to deposit money into account
        :param amount: amount of money to be deposited
        :return: returns if transaction was successful
        """
        try:
            self.account_balance += amount  # 0.00 + amount in form of #.##

            if self.account_balance > 0:
                return True
            else:
                self.account_balance = 0
                return False

        except TypeError:
            print('Enter a valid whole or decimal number')
            return False

        except ValueError:
            print('Enter a valid number greater than zero')
            return False

        except:
            return False

    def withdraw(self, amount):
        """
        Function to withdraw money from account
        :param amount: amount of money to be withdrawn
        :return: returns if transaction was successful
        """
        try:
            if amount > 0:
                if self.account_balance >= amount:
                    self.account_balance -= amount  # 0.00 + amount in form of #.##
                    return True
                else:
                    self.account_balance = 0
                    return False
            else:
                return False

        except TypeError:
            print('Enter a valid whole or decimal number')
            return False

        except ValueError:
            print('Enter a valid number greater than zero and less than or equal to your balance')
            return False

    def get_balance(self):
        """
        Gets current account balance
        :return: returns balance
        """
        return self.account_balance  # number in form of #.##

    def get_name(self):
        """
        Gets current account name
        :return: returns name
        """
        return self.account_name  # 'Name'
