import datetime


class Payment:
    """
    Информация о транзакции
    """
    def __init__(self, trans_date, trans_desc, trans_from, trans_to, trans_amount, trans_curr):
        self.payment_date = trans_date
        self.payment_desc = trans_desc
        self.payment_from = trans_from
        self.payment_to = trans_to
        self.payment_amount = trans_amount
        self.payment_curr = trans_curr

    def from_info(self):
        if self.payment_from == 'No data':
            card = 'No data'
        else:
            if self.payment_from[0:4] == 'Счет':
                len_number = 20
            else:
                len_number = 16
            card_number = self.payment_from[len(self.payment_from) - len_number:len(self.payment_from)]
            card_name = self.payment_from.replace(card_number, '')
            if len_number == 16:
                card_number = card_number[0:6] + '******' + card_number[12:16]
                card_number = ' '.join(card_number[i * 4:(i + 1) * 4] for i in range(4))
            else:
                card_number = '****************' + card_number[16:20]
                card_number = ' '.join(card_number[i * 4:(i + 1) * 4] for i in range(5))
            card = card_name + card_number
        return card

    def to_info(self):
        if self.payment_to[0:4] == 'Счет':
            len_number = 20
        else:
            len_number = 16
        card_number = self.payment_to[len(self.payment_to) - len_number:len(self.payment_to)]
        card_name = self.payment_to.replace(card_number, '')
        if len_number == 16:
            card_number = card_number[0:6] + '******' + card_number[12:16]
            card_number = ' '.join(card_number[i * 4:(i + 1) * 4] for i in range(4))
        else:
            card_number = '****************' + card_number[16:20]
            card_number = ' '.join(card_number[i * 4:(i + 1) * 4] for i in range(5))
        card = card_name + card_number
        return card

    def get_date(self):
        payment_date = datetime.datetime.strptime(self.payment_date, '%Y-%m-%dT%H:%M:%S.%f')
        return str(payment_date.date())

    def payment_info(self):
        return f'{Payment.get_date(self)} {self.payment_desc}\n' \
               f'{Payment.from_info(self)} -> {Payment.to_info(self)}\n' \
               f'{self.payment_amount} {self.payment_curr}\n'
