import pytest
from account import *


class Testing:

    def setup_method(self):
        self.acc1 = Account('James')
        self.acc2 = Account('Carrie')

    def teardown_method(self):
        del self.acc1
        del self.acc2

    def test_init(self):
        assert self.acc1.get_name() == 'James'
        assert self.acc1.get_balance() == 0
        assert self.acc2.get_name() == 'Carrie'
        assert self.acc2.get_balance() == 0

    def test_deposit(self):
        assert self.acc1.deposit(30) is True
        assert self.acc1.get_balance() == 30

        assert self.acc2.deposit(-30) is False

    def test_withdraw(self):
        assert self.acc1.withdraw(30.5) is False
        assert self.acc1.deposit(30) is True
        assert self.acc1.withdraw(20.5) is True
        assert self.acc1.get_balance() == 9.5

        assert self.acc2.withdraw(-10.5) is False
        assert self.acc2.withdraw(0) is False

