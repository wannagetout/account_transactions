from payment import Payment
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.payment = Payment('2019-08-26T10:50:58.294041',
                               'Перевод организации',
                               'Maestro 1596837868705199',
                               'Счет 64686473678894779589',
                               '31957.58', "руб.")

    def test_rom_info(self):
        self.assertEqual(self.payment.from_info(), 'Maestro 1596 83** **** 5199')

    def test_to_info(self):
        self.assertEqual(self.payment.to_info(), 'Счет **** **** **** **** 9589')

    def test_get_date(self):
        self.assertEqual(self.payment.get_date(), '2019-08-26')

    def test_payment_info(self):
        self.assertEqual(self.payment.payment_info(), '''2019-08-26 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **** **** **** **** 9589\n31957.58 руб.\n''')


